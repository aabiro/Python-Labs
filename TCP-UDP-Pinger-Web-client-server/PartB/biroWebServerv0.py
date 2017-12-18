# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:15:13 2017

@author: aaryn
"""
#browser and client linking

#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)


#Prepare a sever socket
#bind and listen
serverSocket.bind(('127.0.0.1', 6789))
serverSocket.listen(5)


while True:
    #Establish the connection
    
    connectionSocket, addr =  serverSocket.accept()
    print 'Ready to serve...'

    try:
        
        message =  connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        print 'Content sent to the client' 
        
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")

        #Close client socket
        connectionSocket.close()
serverSocket.close()

sys.exit() #Terminate the program after sending the corresponding data