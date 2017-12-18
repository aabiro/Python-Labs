# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:15:13 2017

@author: aaryn
"""
#browser and client linking

#import socket module
from socket import *
import sys # In order to terminate the program
import threading
import time

#performs mulithreaded serving from port 6789 increasing by one after each call.

class ConnectionThread (threading.Thread) :
    
    def __init__ (self, port, connectionSocket):
        threading.Thread.__init__(self)
        self.connectionSocket = connectionSocket
        self.port = port #incremented from server call
        print 'new connection thread initiated..'
        print

    
    def run (self):
        print "new connection thread now waiting:", self.port
        try:
                
            message =  connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()
            
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
    
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            
            connectionSocket.close()
    
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            #Send response message for file not found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
            connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
    
            #Close client socket
            connectionSocket.close()

# MAIN THREAD
serverSocket = socket(AF_INET, SOCK_STREAM)
PORT = 6789
serverSocket.bind(('127.0.0.1', PORT))
serverSocket.listen(5)


while True:
    #Establish the connection
    #this is the server working, needs to do the same with different port number each time it is called
        
    connectionSocket, addr =  serverSocket.accept()
    print 'Main thread: Ready to serve...'

    try:
        #connection established, prepare the thread
        
        #create new thread
        cThread = ConnectionThread(PORT, connectionSocket) 
        #start new thread
        cThread.start()

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")

        #Close client socket
        connectionSocket.close()
serverSocket.close()

sys.exit()

