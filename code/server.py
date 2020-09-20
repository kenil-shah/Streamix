from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, emit
from engineio.payload import Payload

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

Payload.max_decode_packets = 100

socketio = SocketIO(app)

@socketio.on('image')
def handle_image(data):
    emit('new', data)


@app.route('/')
def hello_world():
    return render_template("test.html")


if __name__ == '__main__':
    socketio.run(app)