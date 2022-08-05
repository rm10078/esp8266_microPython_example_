import socket
import network
import ujson
from time import sleep

#wifi connection------------------------------------------------------
sta=network.WLAN(network.STA_IF)
if not sta.active():
    sta.active(True)
sta.connect("Rajib","rajib@7224")

while not sta.isconnected():
    print("wait....")
print(sta.ifconfig())
#End wifi connection-------------------------------------------------------

#Function for get data-----------------------------------------------------
def http_get(url,raw_data=False):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    d_out=""
    while True:
        data = s.recv(1000)
        if data:
            d_out+=str(data, 'utf8')
        else:
            break
    s.close()
    #Fillter only page content
    tem_str=''
    for i in range(len(d_out)):
        if d_out[i]=='{':
            for j in range(i,len(d_out)):
                tem_str+=d_out[j]
    if raw_data:
        #Return raw data if you need
        return(d_out)
    else:
        #convert the string into dict
        m=ujson.loads(tem_str)
        return(m)
#End Function for get data-----------------------------------------------------



f=http_get('https://www.worldtimeapi.org/api/timezone/Asia/Kolkata')
print(f)

print(type(f))

print(f["datetime"])