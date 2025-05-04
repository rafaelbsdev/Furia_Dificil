from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    # Implementar lógica de cadastro posteriormente
    return jsonify({"status": "success"}), 200

@app.route('/buscar', methods=['POST'])
def buscar():
    # Implementar lógica de busca posteriormente
    return jsonify([]), 200

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
