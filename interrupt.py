from machine import Pin
from time import sleep

isrpin=Pin(12,Pin.IN)
led=Pin(2,Pin.OUT)

def fun(C):
    print("Irq is call",C)
    led.value(not led.value())
    
isrpin.irq(trigger=Pin.IRQ_RISING, handler=fun)


while True:
    sleep(1000)
