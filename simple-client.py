import argparse
import socket
import sys

# object
parser = argparse.ArgumentParser(description="HTTP Client")

# arguments 
parser.add_argument("-i", "--ip", required=True, type=str, help="Server IP address")
parser.add_argument("-p", "--port", required=True, type=int, help="Server Port")
parser.add_argument("-f", "--file", required=True, type=str, help="Filename to request")


# parse arguments
args = parser.parse_args()

# create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(5)

# connect to host
client_socket.connect((args.ip, args.port))

# create GET request
request = 'GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(args.file, args.ip)

# send the GET request
client_socket.send(request.encode())

# recieve respons from server + print respons
respons = client_socket.recv(4096).decode()
print(respons)

# close socket
client_socket.close()


    