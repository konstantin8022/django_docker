from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from checker import Checker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def status_was_changed(status):
        emit("status", status, broadcast=True)

@socketio.on('location')
def test_message(message):
    c.check(message['data']['lat'], message['data']['lon'])

@socketio.on('connect')
def test_connect():
    emit('response', {'data': 'Connected'}, broadcast=True)

@socketio.on('disconnect')
def test_disconnect():
    emit('response', {'data': 'DisConnected'}, broadcast=True)


if __name__ == '__main__':
    c = Checker()
    c.output = status_was_changed
    socketio.run(app, host="0.0.0.0")