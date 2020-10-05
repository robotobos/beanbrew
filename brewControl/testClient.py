import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.109', 8334))

s.send(bytes("coffee_pot_off","utf-8"))

s.close