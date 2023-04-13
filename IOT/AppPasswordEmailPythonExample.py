#Majid Reza Barghi
#11/17/2022
#CS101 Emailer Client with Google smtp emailer and updated app-password security
#The Goal of this was to send sensor data and an email Alert to the users emails
#For demonstration purposes only, and introduce students to Microcontrollers, Serial commincation,and Email Automation

import smtplib
import time
import serial

#MAKE SURE THAT YOUR PICO IS RUNNING THE PROGRAM IN THE BACKGROUND.
#TO DO SO, RUN THE PROGRAM WHEN CONNECTED TO PICO AND JUST SWITCH TO
#PYTHON ENVIROMENT ON THE BOTTOM LEFT OF THONY TO DISCCONNECT
#IF YOU DON'T THIS WILL NOT WORK

# Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'majidrezabarghi@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = 'gcduqsujuwvcibtz' #change this to match your gmail app-password

# Declaring and Initializing Serial Commincation with Pico
# To find your port number
#******* Windows**********
# Press the windows home key and Search "Device Manager"
# Go to Ports and you will see several ports unplug your pico and plug back in again
# The port that disapears and reapears (The number may have changed) will be the COM we need to use
#******* Mac **************
# Open the Terminal on Mac
# type in the following command ls /dev/tty.usb* 
# This will display all our USB Devices connected to the MAC
# NOTE: PERMISSIONS MAY BE NEEDED, to do so just do a chmod 755 to give read write privilages to the file
#******* Linux ************
# Open the Terminal 
# type in the following command: ls /dev/tty.*
#NOTE: PERMISSIONS MAY BE NEEDED, to do so just do a chmod 755 to give read write privilages to the file

ser = serial.Serial(
    port = 'COM9',\
    baudrate =115200,\
    parity = serial.PARITY_NONE,\
    stopbits = serial.STOPBITS_ONE,\
    bytesize = serial.EIGHTBITS,\
    timeout=0)

print("connected to Raspberry Pico on: " + ser.portstr)

class Emailer:
    def sendmail(self, recipient, subject, content):

        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,"MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

# Declaring Emailer Class

sender = Emailer()


# ================================================================
# This where we input settings on who we will be sending it to.

sendTo = 'majidrezabarghi@gmail.com'
emailSubject = "Hello World"
emailContent = "The value, you measured is: "

try:
    while True:
        message = ser.readline()
        print(message)
        temp = message.decode("UTF-8")
        if len(temp)!=0:
            if temp[0] == 'M':
                emailContent = emailContent + temp[1:]
                sender.sendmail(sendTo,emailSubject,emailContent)
                print("email sent")
        time.sleep(1)
    ser.close()
except KeyboardInterrupt:
    print("Exiting Program.....")
    ser.close()