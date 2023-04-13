from machine import Pin
import utime

class UltraSonic:
    
    def __init__(self,ECHO,TRIG,DEBUG=False):
        self.DEBUG = DEBUG
        self.TRIG = Pin(TRIG,Pin.OUT) 
        self.ECHO = Pin(ECHO,Pin.IN)
        print("object made")

    def get_distance(self):
        self.TRIG.low()
        utime.sleep_us(5)
        self.TRIG.high() 
        utime.sleep_us(5)
        self.TRIG.low()
        while self.ECHO.value()== 0:
            signaloff = utime.ticks_us()
        while self.ECHO.value() == 1:
            signalon = utime.ticks_us()
        timepassed = signalon - signaloff
        distance = (timepassed * .0343) / 2
        if self.DEBUG == True:
            print("the distance from the object is: ",distance,"cm")
        return distance