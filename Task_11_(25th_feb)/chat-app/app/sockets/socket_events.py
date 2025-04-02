from flask_socketio import SocketIO, join_room, leave_room, send
from app.services.chat_service import ChatService

socketio = SocketIO(cors_allowed_origins="*")

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    send({'msg': f"{data['username']} joined {room}"}, room=room)

@socketio.on('message')
def handle_message(data):
    ChatService.save_message(data['room'], data['username'], data['msg'])
    send({'username': data['username'], 'msg': data['msg']}, room=data['room'])

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)
    send({'msg': f"{data['username']} left {room}"}, room=room)
