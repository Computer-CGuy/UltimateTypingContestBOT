import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socka = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
nop = ('localhost',58561)
socka.bind(nop)
sock.listen(1)
socka.listen(1)
while True:
    connection, client_address = sock.accept()
    #connection, client_address = socka.accept()
    try:
        print(client_address)
        while True:
            data = connection.recv(10006)
            if(not str(data)=="b''"):
                #connection.sendall(data)
                connection.sendall(" GET / HTTP/1.1\r\nHost: www.youtube.com\r\n\r\n ".encode())
                print(data.decode("utf-8") )
    except Exception as exceptions:
        print(exceptions)
        pass
