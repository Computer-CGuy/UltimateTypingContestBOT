import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(server_address)
sock.connect(server_address)
try:

    # Send data
    message = b'This is the message.  It will be repeated.'
    print(message)
    sock.sendall(message)

except Exception as exceptions:
    print(exceptions)
    pass
