from flask import Flask, Response, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'afsdjk02934857676jdfhgieurnnr8402984hh48hriuausdfjkruioiuweyrtoiuyweritywerthujertgyuewrouisdfhgiushdfiougdfouiphsdrpoiuh'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)
if __name__ == '__main__':
	socketio.run(app)
	#host='0.0.0.0', port=3000
