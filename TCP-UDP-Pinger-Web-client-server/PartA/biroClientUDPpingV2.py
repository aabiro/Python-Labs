# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:12:29 2017

@author: aaryn
"""

#implement the client
import time
from socket import *

HOST = '127.0.0.1'
PORT = 12000

#create my client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)


# To set waiting time of one second for reponse from server 
clientSocket.settimeout(1)

#heartbeat-sleep for 3 seconds then send again - serever records the sequence number / time of the pacjet
#print SEQUENCE NUMBER : number/ time

# Declare server's socket address
remoteAddr = ('Localhost', 12000)

# Ping ten times
for i in range(10):

    sendTime = time.time()
    message = 'sequence number ' + str(i) + " " + str(time.strftime("%H:%M:%S"))
    clientSocket.sendto(message, remoteAddr)
    

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
        
    time.sleep(3)
