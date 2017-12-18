# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:47:33 2017

@author: aaryn
"""
from socket import *
import sys

#TCP Connection
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number/ hotsname from command line prompt
serverPort = int(sys.argv[2])
serverHost = sys.argv[1]                        


serverSocket.bind((serverHost, serverPort))

serverSocket.listen(1)

while True:
	print ('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()

	try:

		message =  connectionSocket.recv(1024)
      #print the server response
		print ('Server response is: ')
		print (message)

      #recieve filename from the command line prompt
		filename = "/" + sys.argv[3]

		f = open(filename[1:])
		# Store the entire contenet of the requested file in a temporary buffer
		outputdata = f.read()
		# Send the HTTP response header line to the connection socket
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
 
		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i])
		connectionSocket.send("\r\n")
		
		# Close the client connection socket
		connectionSocket.close()

	except IOError:
		# Send HTTP response message for file not found
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
		connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
		# Close the client connection socket
		connectionSocket.close()

serverSocket.close()  

