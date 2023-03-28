from pathlib import Path
import os
import logging
from definitions import ROOT_DIR
from flask import Flask
from flask_socketio import SocketIO
from .socketHandler import SocketHandler

def path():
    #root= os.path.abspath(os.path.dirname(__file__))
    print('Root',ROOT_DIR)
    root = Path(ROOT_DIR)
    src = os.path.join(root,'static')   
    return src


app = Flask(__name__,static_folder=path(),static_url_path='')
sio = SocketIO(app,logger=False,engineio_logger=False)

def start_server( server_secret:'str',host='0.0.0.0', port='5001'):
    global app
    global sio
 #   global scannerDB
    app.secret_key=server_secret
    #scannerDB=database
    sio.run(app,host=host, port=port) 

SocketHandler(sio)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/') 
def home():
    return app.send_static_file('index.html') 

if __name__ == '__main__': 
    print('Started')
    sio.run(app,host='0.0.0.0', port='5001')  # Start the server Host 0.0.0.0 to listen on machine ip