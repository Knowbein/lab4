# File Transfer Client
def send_file_to_server(file_path, host='127.0.0.1', port=65432):
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        try:
            with open(file_path, "rb") as f:
                while chunk := f.read(1024):
                    client_socket.sendall(chunk)
            print(f"File '{file_path}' sent successfully.")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"Error during file transfer: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path of the file to send: ").strip()
    send_file_to_server(file_path)
