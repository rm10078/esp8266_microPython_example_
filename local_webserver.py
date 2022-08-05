import network,ujson
import usocket as socket
from time import sleep_ms


def page_data():
    txt="""
            <!DOCTYPE html>
    <html>
      <style>
        body{
          text-align: center;
        }
        h1{
          font-size: 3vw;
        }
        h1{
          font-size: 1.5vw;
        }
        a{
          background-color: rgb(0, 0, 0);
          color: rgb(255, 255, 255);
          margin-top: 2vw;
          padding: 3vw;
          display: inline-block;
          text-decoration: none;
          font-size: 2vw;
        }
      </style>
      <title>Home page</title>
    <body>
    <h1>Esp8266 webserver</h1>
    <h3 class="feedback">value</h3>
    <a href="/gpio02">GPIO02</a>
    <h3 class="feedback">value</h3>
    <a href="/gpio16">GPIO16</a>
    <h3 class="feedback">value</h3>
    <a href="/gpio02">GPIO12</a>
    <h3 class="feedback">value</h3>
    <a href="/gpio02">GPIO13</a>
    </html>"""
    return txt

def fil_data(g):
    ms=''
    s1=''
    for i in range(len(g)):
        if i+7<len(g):
            s1=''
            k=0
            while k<7:
                s1+=g[i+k]
                k+=1
        if s1=='http://':
            for j in range(i,(len(g)-5)):
                t00=str(g[j]+g[j+1]+g[j+2]+g[j+3]+g[j+4])
                if t00!="Accep":
                    ms+=g[j]
                else:
                    break
    return ms[:-4]



ssid='Rajib'
password='rajib@7224'

#wifi connection
sta=network.WLAN(network.STA_IF)
ap=network.WLAN(network.AP_IF)
if ap.active():
    ap.active(False)
    
sta.connect(ssid,password)

while not sta.isconnected():
    pass
print(sta.ifconfig())




#Web server setup----------------------------------------------------

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)

#Web server setup end------------------------------------------------


while True:
    conn,addr=s.accept()
    request0=conn.recv(1024)
    request=str(request0)
    response=page_data()
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("content-type:text/html\n")
    conn.send("Connection:close\n\n")
    conn.sendall(response)
    conn.close()
    #print(request)
    print(fil_data(request))
    