import socket 

HOST, PORT = 'localhost', 8080

# Create a socket and bind it to the host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the socket options
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

# Print a message indicating the server is listening
print(f"Server listening on {HOST}:{PORT}")


# Handle incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Handle the client request (simplified for this example)
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received request:\n{request}")

    # Send a simple response
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World! This is my first HTTP server."
    client_socket.send(response.encode('utf-8'))

    # Close the client connection
    client_socket.close()