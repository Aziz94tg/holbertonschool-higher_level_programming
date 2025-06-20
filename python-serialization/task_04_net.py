import socket
import json

# Server-side function
def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}...")

        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        data = conn.recv(1024)  # Receive up to 1024 bytes
        if data:
            try:
                received_dict = json.loads(data.decode('utf-8'))
                print("\nReceived Dictionary from Client:")
                print(received_dict)
            except json.JSONDecodeError:
                print("Failed to decode JSON data.")
        conn.close()
    finally:
        server_socket.close()

# Client-side function
def send_data(dictionary, host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        serialized_data = json.dumps(dictionary)
        client_socket.sendall(serialized_data.encode('utf-8'))
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()

