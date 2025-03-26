import socket
import threading

# function to handle client request
def handleClient(client_socket):

    # receive the request from the client
    request = client_socket.recv(1024).decode()
    print("Received request:")
    print(request)

    # basic HTTP response with plain only
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHeyyyy, a simple web server"

    client_socket.send(response.encode())   # send response to the client
    client_socket.close()                   # close the client socket

# main function to start the server
def main():
    # create a TCP server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       

    # bind the socket to localhost on port 8080   
    server_socket.bind(("localhost", 8080))

    # start listening for incoming connections
    server_socket.listen(5)

    print("Server started on http://localhost:8080")

    # infinite loop t oaccept multiple client connections 
    while True:
        client_socket, _ = server_socket.accept()

        # create a new thread to handle the client request
        threading.Thread(target=handleClient, args=(client_socket,)).start()
        
# run the server if the script is executed directly
if __name__ == "__main__":
    main()
