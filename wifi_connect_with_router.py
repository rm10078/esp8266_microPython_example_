
def wifi_connection(ssid,password,update=False):
    import network
    sta=network.WLAN(network.STA_IF)
    if not sta.active():
        sta.active(True)
    if update and sta.active()==True:
        sta.connect(ssid,password)
    while not sta.isconnected():
        pass
    
    return sta.ifconfig()

print(wifi_connection('SSID','PASSWORD',True))
