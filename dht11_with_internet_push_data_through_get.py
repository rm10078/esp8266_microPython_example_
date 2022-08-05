import helper as hp
import dht
from machine import Pin,ADC
from time import sleep

#I transfer data to the blink cloud

ssid='Rajib'
password='rajib@7224'

led=Pin(16,Pin.OUT)
adc_pin=ADC(0)
sensor=dht.DHT11(Pin(14))
ip=hp.wifi_connect(ssid,password)
print(ip)
   

while True:
    try:
        sensor.measure()
        tem=sensor.temperature()
        hum=sensor.humidity()
        temm='https://blynk.cloud/external/api/update?token=o11KejlUeC4-iIzO7ID-aDzO6CJM_e__&v1='+str(tem)
        humm='https://blynk.cloud/external/api/update?token=o11KejlUeC4-iIzO7ID-aDzO6CJM_e__&v2='+str(hum)
        r=hp.http_get(temm)
        h=hp.http_get(humm)
    except OSError:
        print("problem")
    adc_value=adc_pin.read()
    """
    r=hp.http_get('https://api.thingspeak.com/update?api_key=LAESAN9FEHX95W58&field1='+str(tem))
    e=hp.http_get('https://api.thingspeak.com/update?api_key=LAESAN9FEHX95W58&field2='+str(hum))
    f=hp.http_get('https://api.thingspeak.com/update?api_key=LAESAN9FEHX95W58&field3='+str(adc_value))
    """

    
    
    gass='https://blynk.cloud/external/api/update?token=o11KejlUeC4-iIzO7ID-aDzO6CJM_e__&v3='+str(adc_value)
    
    led_stat=hp.http_get('https://blynk.cloud/external/api/get?token=o11KejlUeC4-iIzO7ID-aDzO6CJM_e__&v0')
    led_status=int(led_stat[-1:])
    led.value(led_status)
    q=hp.http_get(gass)
    
    print("Temperature :",tem," C humidity : ",hum," % ADC Value :",adc_value)
    sleep(1)
    
    """
    #define BLYNK_TEMPLATE_ID "TMPLMcFoX4Qf"
    #define BLYNK_DEVICE_NAME "iotpro"
    #define BLYNK_AUTH_TOKEN "o11KejlUeC4-iIzO7ID-aDzO6CJM_e__"
    """