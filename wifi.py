import network

sta_if=network.WLAN(network.STA_IF) #create a instance
ap_if=network.WLAN(network.AP_IF)
print(sta_if.active())  #check what is active now acces point or connetc with router

print(ap_if.active())


print(ap_if.ifconfig())
#Result of ifconfig function
#('192.168.4.1', '255.255.255.0', '192.168.4.1', '208.67.222.222')
#  ip address      subnetmask        gateway         DNS