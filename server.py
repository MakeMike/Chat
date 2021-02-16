from flask import Flask, Response, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'afsdjk02934857676jdfhgieurnnr8402984hh48hriuausdfjkruioiuweyrtoiuyweritywerthujertgyuewrouisdfhgiushdfiougdfouiphsdrpoiuh'
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def server():
	return render_template("msgindex.html")
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, threaded=True)
	#host='0.0.0.0', port=3000
