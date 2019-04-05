
# Server intended to run on http://127.0.0.1:5000

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('video.html')


@app.route('/video', methods=['GET', 'POST'])
def video():
    '''
    Handle video/image data sent through the client.
    To be done:
    > Use `requests` to handle data sent from the client.
    > Also, enforce data-type to be consistent across network and browser. 

    Possible options are:

        1. Use `requests` to POST data.
        2. Manually configure render_template to work according to
           image/video data.

    Note that this route only has the work of displaying the data on
    the webpage, and has nothing to do with the camera.
    '''

    '''
    Argument of `Response` should contain the `.tobytes()`
    string to render correctly on the browser.
    '''
    # if flask.request.method == 'POST':
    raw_data = flask.request.get_data()
    # print(raw_data)
    # return flask.Response(gen(VideoCamera()),
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')

    # ERR_POSS:  use (...) with proper_datas
    proper_data = (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + raw_data + b'\r\n\r\n')


    return flask.Response(proper_data,
                          mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=True)
