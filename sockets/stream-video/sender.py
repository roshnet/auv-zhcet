import socket
from camera import VideoCamera


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5000

client.connect((host, port))

camera = VideoCamera()


while True:
    frame = camera.get_frame()
    client.send(frame)

