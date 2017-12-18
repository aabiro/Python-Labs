# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:12:29 2017

@author: aaryn
"""

#implement the client
import time
import sys
from socket import *

HOST = '127.0.0.1'
PORT = 12000

#create my client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)


# To set waiting time of one second for reponse from server
clientSocket.settimeout(1)

# Declare server's socket address
remoteAddr = ('Localhost', 12000)

# Ping ten times
for i in range(10):
    
    sendTime = time.time()
    messageToCap = 'ping ' + str(i + 1) + " " + str(time.strftime("%H:%M:%S"))
    clientSocket.sendto(messageToCap, remoteAddr)
    
    try:
        data, server = clientSocket.recvfrom(1024)
        receivedTime = time.time()
        roundTripTime = receivedTime - sendTime
        print "Message Received", data
        print "Round Trip Time", roundTripTime
        print
    
    except timeout:
        print 'REQUEST TIMED OUT'
        print