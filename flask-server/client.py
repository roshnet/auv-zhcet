import socket
import cv2
import requests
import json
# from camera import VideoCamera

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Host and Port to throw data to.
TARGET_HOST = 'localhost'
TARGET_PORT = 5000

TARGET_URL = '{}:{}'.format(TARGET_HOST, TARGET_PORT)

# client.connect((TARGET_HOST, TARGET_PORT))
# print('Ready to send data on {}:{} ...'.format(TARGET_HOST,
#                                                TARGET_PORT))


# Now, start capturing video and send to server.
# Can also use `requests` to send image frames.

# cam = VideoCamera()


def throw_frames():
    '''
    Infinitely returns all frames it captures, to the server,
    encoded by `tobytes()` method.
    '''
    i = 1
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, image = cap.read()
        ret, jpeg = cv2.imencode('.jpg', image)

        headers = {
            'Content-Type': 'application/octet-stream',
            # 'Content-length': '100000'
        }
        # Headers don't need to be specified in 2.4.2


        payload = jpeg.tobytes()
        # Test this format later.

        # payload = {
        #     'bytecode': str(jpeg.tobytes())
        # }

        # Ensure `requests==2.4.2` if using `json=payload` as arg.
        response = requests.get('http://localhost:5000',
                                 data=payload,
                                 headers=headers)



        # yield (b'--frame\r\n'
        #        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



        # BASIC IMSHOW TESTING:
        # ret, frame = cap.read()
        # cv2.imshow('GGG', frame)

        # if cv2.waitKey(1) &0xFF == ord('q'):
        #     break

    cap.release()
    cv2.destroyAllWindows()

throw_frames()
