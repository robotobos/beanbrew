import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.1.136', 8334)
print('starting socker server')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from: ', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received data: ', data)
            if data:
                print('implement send data back')
                #connection.sendall(data)
            else:
                print("no more data")
                break
            
    finally:
        # Clean up the connection
        connection.close()