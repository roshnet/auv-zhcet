import socket
from camera import VideoCamera
import flask


# SERVER config:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5000

server.bind((host, port))
server.listen(500)

camera = VideoCamera()

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



# Processing video frame-by-frame

while True:
    client_socket, addr = server.accept()

    recv_frame = client_socket.recv(1024)

    # All footage is thrown here.

    # PROBLEM: How to make flask take over the next part of 
    # rendering the footage to the webpage on calling the URL. 


