# File Transfer Server
def start_file_server(host='127.0.0.1', port=65432):
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            save_file_from_client(conn, addr)

def save_file_from_client(conn, addr):
    with conn:
        try:
            with open("received_file.txt", "wb") as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print(f"File transfer complete from {addr}")
                        break
                    f.write(data)
        except Exception as e:
            print(f"Error handling file transfer from {addr}: {e}")

if __name__ == "__main__":
    start_file_server()
