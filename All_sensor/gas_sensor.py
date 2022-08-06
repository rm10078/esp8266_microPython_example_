from machine import Pin,ADC
from time import sleep_ms

sensor=ADC(0)

while True:
    value=sensor.read()
    print(value)
    sleep_ms(50)