import machine
import network
import socket

#set up gpio pins
p22_green = machine.Pin(22, machine.Pin.OUT)
p23_red = machine.Pin(23, machine.Pin.OUT)
p34_yellow = machine.Pin(13, machine.Pin.OUT)
#red for netowkr off 
p23_red.value(1)

#turn on wlan
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

#read network config file
file=open("config.txt")
apinfo=file.read()
apinfo=apinfo.split(',')
ssid=apinfo[0]
pw=apinfo[1]

print('connecting to network...')
wlan.connect(ssid, pw)
while not wlan.isconnected():
    pass
print('network config:', wlan.ifconfig())
p22_green.value(1)
p23_red(0)

#then bind socket listener
if wlan.isconnected():
    deviceip=wlan.ifconfig()[0]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((deviceip, 8334))
    sock.listen(5)
    print("socket listening on port 8334 on ", deviceip)
else:
    print("network connect failed")

#loop connections forever
while True:
    print("waiting for connection")
    conn, addr = sock.accept()
    full_msg=''
    while True:
        msg = conn.recv(8)
        if len(msg) <= 0:
            break
        full_msg += msg.decode("utf-8")
    print(full_msg)

    if(full_msg=="coffee_pot_on"):
        print("coffee pot turning on")
        p34_yellow.value(1)
    
    if(full_msg=="coffee_pot_off"):
        print("coffee pot turning on")
        p34_yellow.value(0)
    
