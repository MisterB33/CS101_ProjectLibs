from machine import Pin
from time import sleep
import dht

import network
import socket

import Newurequests as urequests #updated urequests library. 

#Enter Wifi information. 
ssid = 'YOURHOTSPOT'
password ="HOTSPOTPASSWORD"

DEBUG = False #set this parameter to False to turn off debug outputs. 

APIkey= "APIKEYHERE"

#initializing the wlan for internet connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

#Setting up the DHT22 sensor 
sensor = dht.DHT22(Pin(2))

if DEBUG == True:
    accessPoints = wlan.scan() #perform a WiFi Access Points scan

#this loop prints each AP found in a single row on 
    for ap in accessPoints: 
        print(ap)
    
def connect():
    wlan.connect(ssid,password)
    while wlan.isconnected() == False:
        print('waiting for connnection..')
        sleep(1)

try:
    print("connecting...")
    connect()
except KeyboardInterrupt:
    machine.reset()

print("Connection Success")



while True:
    sensor.measure()
    temp = sensor.temperature() #updating temperature data 
    hum = sensor.humidity() #updatating Humidity data 
    print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))
    sleep(10) #update sensor data every 10 seconds 
    GetReq = "https://api.thingspeak.com/update?api_key="+APIkey+"&field1="+str(temp)+"&field2="+str(hum)
    response = urequests.get(GetReq)