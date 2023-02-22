from flask import Flask, render_template
from flask_socketio import SocketIO,emit
import json,cppimport
import scramble


clib = cppimport.imp("clib")


app = Flask(__name__,
            static_url_path='', 
            static_folder='static',)
sapp = SocketIO(app)

@app.route("/room")
def room():
	return render_template("room.html")

@app.route("/")
def index():
	return render_template("index.html")


	
@sapp.on('setEVN')
def sevn(d):
	i = int(d["id"])
	evn = d["evn"]
	clib.set_event(i,evn)

@sapp.on("update")
def handle_ge(data):
	d = json.loads(data['data'])
	d['id'] = str(d['id'])
	clib.parse(d)
	
	
	emit("retupdate",[json.dumps(clib.get(int(d["id"]))),int(d["id"])], broadcast=True)

@sapp.on("newr")
def handle_nr(data):
	d = int(data['data'])
	clib.clear(d)
	
	emit("retupdate",["{}",d], broadcast=True)
	event  = clib.get_event(d)
	scr = scramble.scrambled[event]()
	emit("newscramb",[scr,d],broadcast=True)


@sapp.on("chatR")
def handle_chatr(data):
	d = int(data['id'])
	msg = data["msg"]
	emit("chat",[msg,d], broadcast=True)



	
sapp.run(app,host="0.0.0.0")
