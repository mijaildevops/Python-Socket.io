from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

countmsj = 0

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg, countmsj):
    print('Message: ' + msg)
    countmsj = 1 + countmsj
    print(countmsj)
    send(msg, broadcast = True)

if __name__ == '__main__':
    socketio.run(app.run(host='0.0.0.0', port=5000, debug=True))
