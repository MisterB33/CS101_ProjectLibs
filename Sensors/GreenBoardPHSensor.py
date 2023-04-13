import machine
import utime

adc_calib = 3.24/65530.0
M = -6.75
B = 24.4

avg_val = 0.0
phvalue = 0.0
avg_Voltage = 0.0

buffer = []

analog_value = machine.ADC(27)

while True:
    for i in range(0,9):
        buffer.append(analog_value.read_u16())
        utime.sleep(.08)
    buffer.sort()  
    avg_val = sum(buffer) / len(buffer)
    buffer.clear()
    avg_Voltage = avg_val*adc_calib
    reading = analog_value.read_u16()     
    print(f"ADC: {reading}")
    print(f"Voltage: {avg_Voltage}")
    phvalue = avg_Voltage*M+B
    print(f"PH Value : {phvalue}")
    utime.sleep(0.25)