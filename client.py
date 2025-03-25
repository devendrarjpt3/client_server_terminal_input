import socket
import sys

def start_client(server_name, port):
    """Connects to the server and sends messages."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_name, port))
        print(f"Connected to {server_name}:{port}")

        while True:
            message = input("To exit (type quit): ")
            client_socket.sendall(message.encode())
            response = client_socket.recv(1024).decode()
            print (f"Server response: {response}")

            if message.lower() == "quit":
                print("Exiting client.")
                break
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py server_name port")
        sys.exit(1)
    try:
        server_name = str(sys.argv[1])
        port = int(sys.argv[2])
        start_client(server_name, port)
    except ValueError:
        print("Error:Enter Valid Value")
        sys.exit(1)
