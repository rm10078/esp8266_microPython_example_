from machine import Pin
from time import sleep

count=0

sensor_a=Pin(12,Pin.IN)
sensor_b=Pin(13,Pin.IN)

led=Pin(2,Pin.OUT)

def calla(C):
    count+=1
    
sensor_a.irq(trigger=Pin.IRQ_RISING, handler=calla)

while True:
    print("Counter value : ",count)
    sleep(500)