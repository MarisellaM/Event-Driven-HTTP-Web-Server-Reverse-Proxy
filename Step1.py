## Goal understand how the raw socket works 
import socket 

HOST = "localhost" 
PORT = 8080

## Hardcode the message to be sent to the server

message = "Hello, this is a test message!"
## Send the message to the server
HARDCODED_MESSAGE = message.encode('utf-8')

def main(): 

    """ Create the raw socket that just spawns a connection to the server to send the message 
    .AF_INET is the address family for IPv4
    .SOCK_STREAM is the socket type for TCP
    These are used to create a TCP socket that can be used to send and receive data over the network."""

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Restart the server with setsockopt to allow the socket to be reused. This is useful when the server is restarted and the socket is still in use. """
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    ## Binding the socket to the specified host and port. This allows the server to listen for incoming connections on the specified address and port. """
    server_socket.bind((HOST, PORT))

    ## The mac queue that is allowed to wait for connecting 
    server_socket.listen(5)

    ## Accepting a connection and receiving the message from the client. 
    print(f"Server is listening on {HOST}:{PORT}...")

    while True: 
        