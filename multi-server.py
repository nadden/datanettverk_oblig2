import socket
import threading

def handleClient(client_socket):
    request = client_socket.recv(1024).decode()
    print("Received request:")
    print(request)

    # Basic HTTP response with text only
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHeyyyy, a simple web server"

    client_socket.send(response.encode())  # Send response
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(5)

    print("Server started on http://localhost:8080")

    while True:
        client_socket, _ = server_socket.accept()
        threading.Thread(target=handleClient, args=(client_socket,)).start()

if __name__ == "__main__":
    main()
