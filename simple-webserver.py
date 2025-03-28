#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket
#Write your code here
serverPort = 8000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)


#End of your code
while True:
	#Establish the connection print('Ready to serve...') connectionSocket, addr = 
	try:
		#Write your code here
		print('Ready to serve...')
		connectionSocket, addr = serverSocket.accept()

		#End of your code
		message = connectionSocket.recv(1024).decode() #Write your code here #End of your code 
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read() #Write your code here #End of your code 

		#Send one HTTP header line into socket
		#Write your code here
		connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())

		#End of your code

		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode()) 
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()


	except IOError:
		#Send response message for file not found
    	#Write your code here
		connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode())
		connectionSocket.send("<html><head></head><body><h1>404 not Found</h1></body></html>\r\n".encode())

    	#End of your code
		
		#Close client socket
        
        #Write your code here
		connectionSocket.close()
		
		#End of your code
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data