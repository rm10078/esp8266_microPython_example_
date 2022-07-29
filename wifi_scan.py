"""
import network

wf=network.WLAN(network.STA_IF)

wf.active(True)
data=wf.scan()

for i in range(len(data)):
    tem=data[i]
    print("ssid : ",tem[0]," Signal :",tem[3])
"""    

#Function for wifi scan

def wifi_scan(ap=False):
    import network

    wf=network.WLAN(network.STA_IF)
    acp=network.WLAN(network.AP_IF)
    if acp.active():
        acp.active(False)
    if not wf.active():
        wf.active(True)
        
    data=wf.scan()
    tem1=[]
    for i in range(len(data)):
        tem=data[i]
        st1=str(tem[0])
        st2=str(tem[3])
        st3=st1[1:]+"  "+st2
        tem1.append(st3)
        
    return tem1

result=wifi_scan()

print(result)
