from app import create_app
from app.sockets.socket_events import socketio

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        from app.models import db
        db.create_all()
    socketio.run(app, debug=True)
