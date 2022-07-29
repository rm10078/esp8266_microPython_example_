import machine,time

#16 2

led=machine.Pin(16,machine.Pin.OUT) #16 is pin number
led2=machine.Pin(2,machine.Pin.OUT)

while True:
    led.value(1)
    led2.value(0)
    time.sleep_ms(500)
    led.value(0)
    led2.value(1)
    time.sleep_ms(500)
    
