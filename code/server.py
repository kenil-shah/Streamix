from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, emit
from engineio.payload import Payload
import numpy
import cv2
import base64
from python_background_pipeline.main import get_segmentation

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

Payload.max_decode_packets = 20

socketio = SocketIO(app)

@socketio.on('image')
def handle_image(data):
    data = base64.b64decode(data)
    jpg_as_np = numpy.frombuffer(data, dtype=numpy.uint8)
    image_buffer = cv2.imdecode(jpg_as_np, flags=1)
    _, data = cv2.imencode('.jpg', image_buffer)
    data = data.tobytes()
    data = base64.b64encode(data)
    data = data.decode('utf-8')
    emit('new', data)


@app.route('/')
def hello_world():
    return render_template("test.html")


if __name__ == '__main__':
    socketio.run(app)