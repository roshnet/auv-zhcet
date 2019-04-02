import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()

# Change port if errors occur.
port = 5000

client.connect((host, port))

client.send('hello'.encode('ascii'))

response = client.recv(1024).decode('ascii')
# `1024` can be less as only text may return from server.


print('Server replied: {}'.format(response))




