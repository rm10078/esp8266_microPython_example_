import machine,time

in_pin=machine.ADC(0)
led_pin=machine.Pin(12)

led=machine.PWM(led_pin)
led.freq(900)

tem=1024/255

while True:
    val=int(in_pin.read()/tem)
    #print(in_pin.read())
    #print(val)
    led.duty(val)
    time.sleep_ms(10)