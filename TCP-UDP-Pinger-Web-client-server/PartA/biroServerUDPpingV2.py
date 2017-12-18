# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:05:41 2017

@author: aaryn
"""

# UDPHeartbeatServer.py

import random
import time
import socket

PORT = 12000

# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('Localhost', PORT))

sequenceNumber = 0

#waiting for message here in while loop
while True:

# Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)    
# Receive the client packet along with the address it is coming from 
    message, address = serverSocket.recvfrom(1024)
    recdTime = time.strftime("%H:%M:%S")
    
    
# Capitalize the message from the client
    message = message.upper()
# If rand is less is than 3, we consider the packet lost and do not respond
    if rand < 3:
        print "LOST PACKET"
        sequenceNumber += 1
        continue
# Otherwise, the server responds    
    serverSocket.sendto(message, address)
    print "SEQUENCE NUMBER:", sequenceNumber, recdTime
    sequenceNumber += 1
    #Assume the client application has stopped - timeout
    serverSocket.settimeout(5)