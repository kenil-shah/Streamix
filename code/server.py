from flask import Flask
from flask import render_template, url_for
from flask_socketio import SocketIO, emit
from engineio.payload import Payload
import numpy
import cv2
import base64
import time
import argparse
import os
from python_background_pipeline.segmenter import get_segmentation


pathtomodel = os.path.join("..", "data", "models", "only_params.pth")
pathtobg = os.path.join(".", "static", "images", "HomeBG.jpg")

def get_args(bgpath):

    args = {}
    args['model'] = pathtomodel
    args['without_gpu'] = True
    args['background_image'] = bgpath
    args['input_resolution'] = 256
    args['camera_resolution'] = [640, 360]
    args['camera_id'] = 0
    args['threshold'] = 0.75

    return args

get_seg = None
staticpath = os.path.join(os.path.abspath("."), "static")
app = Flask(__name__, static_folder=staticpath)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

Payload.max_decode_packets = 100

socketio = SocketIO(app)


@socketio.on('bgimage')
def handle_bgimage(data):
    print(data)
    pathtobg = os.path.join(".", "static", "images", data)
    global get_seg
    get_seg = get_segmentation(get_args(pathtobg))

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
def home():
    return render_template("selectimage.html")

@app.route('/startvideo')
def test():
    return render_template("test.html")

if __name__ == '__main__':
    socketio.run(app)
