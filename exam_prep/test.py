import socketio as io

conn = io.Client()

conn.connect("http://localhost:3000")

conn.emit("send-text", "This is a test")