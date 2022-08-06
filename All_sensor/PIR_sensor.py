from machine import Pin
from time import sleep

PIR_sensor=Pin(12,Pin.IN)
led=Pin(2,Pin.OUT)

def fun(C):
    print("Motion detect",C)
    led.value(not led.value())
    
PIR_sensor.irq(trigger=Pin.IRQ_RISING, handler=fun)


while True:
    sleep(1000)