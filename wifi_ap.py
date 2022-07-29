import network

ac_point=network.WLAN(network.AP_IF)
st=network.WLAN(network.STA_IF)
if st.active():
    st.active(False)
    
if not ac_point.active():
    ac_point.active(True)
    
ac_point.config(essid="acc_point",password="1234abcd")

print(ac_point.ifconfig())
