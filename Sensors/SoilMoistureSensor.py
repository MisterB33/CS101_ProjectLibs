from machine import ADC, Pin
import utime

class MoistureSensor:
    
    
    def __init__(self,PIN,DEBUG=False):
        self.PIN = PIN
        self.DEBUG = DEBUG
        

#Remember This is a capacitive sensor therfore the voltage should go down
#when it is submerged in water. 
    def avg(self,sample):
        return sum(sample)/float(len(sample))
        

    def get_measurement(self):
        samp = []
        soil_adc = ADC(Pin(self.PIN)) # pin for analog 
        utime.sleep(0.5)
        SAMPLESIZE = 30
        conversion_factor = 3.3/(65536.0)
        for x in range(SAMPLESIZE):
            samp.append(soil_adc.read_u16())       
        Voltage = self.avg(samp) * conversion_factor
        if self.DEBUG == True:
            print("Voltage Value os -----> %1.3f" %Voltage)
        return Voltage

    
 