from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import uuid
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import time
from collections import OrderedDict

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')