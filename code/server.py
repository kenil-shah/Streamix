from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, emit
from engineio.payload import Payload
import numpy
import cv2
import base64
import time
import os
from python_background_pipeline.segmenter import get_segmentation


pathtomodel = os.path.join("..", "data", "models", "only_params.pth")
pathtobg = os.path.join("..", "data", "bg_images", "HomeBG.jpg")


def get_args():

    args = {}
    args['model'] = pathtomodel
    args['without_gpu'] = True
    args['background_image'] = pathtobg
    args['input_resolution'] = 256
    args['camera_resolution'] = [640, 360]
    args['camera_id'] = 0
    args['threshold'] = 0.75

    return args


get_seg = get_segmentation(get_args())

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

Payload.max_decode_packets = 100

socketio = SocketIO(app)

@socketio.on('image')
def handle_image(data):
    data = base64.b64decode(data)
    jpg_as_np = numpy.frombuffer(data, dtype=numpy.uint8)
    image_buffer = cv2.imdecode(jpg_as_np, flags=1)
    start = time.time()
    output = get_seg.run_torch(image_buffer)
    end = time.time()
    _, data = cv2.imencode('.jpg', output)
    data = data.tobytes()
    data = base64.b64encode(data)
    data = data.decode('utf-8')
    emit('new', data)


@app.route('/')
def hello_world():
    return render_template("test.html")


if __name__ == '__main__':
    socketio.run(app)
