import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

# Change port in case of errors.
port = 5000

server.bind((host, port))

# Change listening limit (500) as per amount of transmitted data.
server.listen(500)

while True:

    client_socket, addr = server.accept()

    print('Got data from {addr}'.format(addr=addr))

    message = client_socket.recv(1024).decode('ascii')

    print('=================')
    print(message)
    print('=================')

    client_socket.send((message + ', Roshan!').encode('ascii'))

    client_socket.close()
