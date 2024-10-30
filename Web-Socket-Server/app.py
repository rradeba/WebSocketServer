from web_socket_server import WebSocketServer, socketio
from flask import render_template

app = WebSocketServer().create_app()

message_storage = {}

@socketio.on('connect')
def handle_connect():
    print('Client Connected')

@socketio.on('disconnect')  
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    author = data.get('author')  
    message = data.get('message')

    if author and message:
        print(f'New message from {author}: {message}')

        if author not in message_storage:
            message_storage[author] = []
        message_storage[author].append(message)

        socketio.emit('message', data)


@socketio.on('get_user_messages')
def handle_get_user_messages(author):
    
    user_messages = message_storage.get(author, [])
    socketio.emit('get_user_messages', {'author': author, 'messages': user_messages})

@app.route('/')
def index():
    return render_template('WebSocketClient.html')

if __name__ == '__main__': 
    socketio.run(app, debug=True)
