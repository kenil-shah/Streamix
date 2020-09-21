from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, emit
from engineio.payload import Payload
import numpy
import cv2
import base64
import time
import argparse
from python_background_pipeline.main import get_segmentation

def get_args():

    parser = argparse.ArgumentParser(description='Background Matting')
    parser.add_argument('--model',
                        default='C:/Users/Kenil/Desktop/Github/Streamix/data/models/only_par.pth',
                        help='Location of the Trained Model')
    parser.add_argument('--without_gpu', action='store_true', default=True, help='Use CPU')
    parser.add_argument('--background_image',
                        default='C:/Users/Kenil/Desktop/Github/Streamix/data/bg_images/HomeBG.jpg',
                        help='Location of Background Image')
    parser.add_argument('--input_resolution', default=256, help='Input resolution (Higher == Slower == Acccurate)')
    parser.add_argument('--camera_resolution', default=[640, 360],
                        help='Input resolution (Higher == Slower == Acccurate)')
    parser.add_argument('--camera_id', default=0, help='Camera ID to be used')
    parser.add_argument('--threshold', default=0.75, help='Set Threshold')

    args = vars(parser.parse_args())
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
