import machine,time

in_pin=machine.Pin(10,machine.Pin.IN,machine.Pin.PULL_UP)
led=machine.Pin(2,machine.Pin.OUT)

led.value(1)

while True:
    led.value(1)
    print(in_pin.value())
    #led.value(in_pin.value())
    if in_pin.value()==False:
        led.value(0)
    time.sleep_ms(100)