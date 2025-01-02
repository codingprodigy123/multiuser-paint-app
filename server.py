import socket
import threading

HOST = '127.0.0.1'  # Server IP address
PORT = 5000         # Port to listen on

clients = []  # List to store connected clients

def handle_client(client_socket):
    """Handle messages from a client and broadcast to others."""
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            # Broadcast data to all other clients
            for client in clients:
                if client != client_socket:
                    client.send(data)
        except:
            break

    # Remove client from list when disconnected
    clients.remove(client_socket)
    client_socket.close()

def start_server():
    """Start the server and accept incoming connections."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"New connection from {addr}")
        clients.append(client_socket)
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
