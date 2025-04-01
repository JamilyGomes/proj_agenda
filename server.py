from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")

@socketio.on('message')
def handle_message(data):
    print(f"Mensagem recebida: {data}")
    socketio.emit('message', data)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)