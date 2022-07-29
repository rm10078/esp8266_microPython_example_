import machine,time

out_pin=machine.Pin(12)

pwm_out=machine.PWM(out_pin)
pwm_out.freq(999)
while True:
    
    for i in range(0,1024):
        print(i)
        pwm_out.duty(i)
        time.sleep_ms(3)