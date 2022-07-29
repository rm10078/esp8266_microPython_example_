import machine,time

adc_pin=machine.ADC(0)

while True:
    print(adc_pin.read())
    time.sleep_ms(1)