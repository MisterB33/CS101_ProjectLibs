import umail
import time
import network
import dht

from machine import Pin
from time import sleep

#Enter Wifi information. 
ssid = 'HOTSPOTNAME'
password ="HOTSPOTPASSWORD"

#Set up DHT22 Sensor 
sensor = dht.DHT22(Pin(2))

DEBUG = False #set this parameter to False to turn off debug outputs. 

#initializing the wlan for internet connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if DEBUG == True:
    accessPoints = wlan.scan() #perform a WiFi Access Points scan

#this loop prints each AP found in a single row on 
    for ap in accessPoints: 
        print(ap)
    
def connect():
    wlan.connect(ssid,password)
    sleep(1)
    while wlan.isconnected() == False:
        print('waiting for connnection..')
        sleep(1)

try:
    print("connecting...")
    connect()
    sleep(1)
except KeyboardInterrupt:
    print("failed to connect")

print("Connection Success")

APPPASSWORD = "YOURAPPPASSWORDHERE"
SENDER = 'my@gmail.com'
RECEIVER = 'someonesemail@gmail.com'

while True: 
    smtp = umail.SMTP('smtp.gmail.com', 587, username= SENDER, password=APPPASSWORD)
    smtp.to(RECEIVER)
    # updating sensor for this example we are using a temperature sensor, and simple True of False would work as well.  
    sensor.measure()
    SensorVal = sensor.temperature()
    #Create a Boolean our of this
    BoolSens = SensorVal > 20.0
    print(SensorVal)
    if BoolSens :
        smtp.send("This is an example.")
        print("email sent!")
        smtp.quit()
    time.sleep(5)