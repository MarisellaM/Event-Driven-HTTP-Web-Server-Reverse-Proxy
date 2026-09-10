import socket 

HOST = "localhost" 
PORT = 8080

## Hardcode the message to be sent to the server

message = "Hello, Server!"
## Send the message to the server
HARDCODED_MESSAGE = message.encode('utf-8')

## handle the socket connection and send the message
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(HARDCODED_MESSAGE)
    data = s.recv(1024)
    print(f"Received: {data.decode('utf-8')}")
    