# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:12:29 2017

@author: aaryn
"""

#implement the client
import time
import sys
from socket import *
import numpy
import matplotlib.pyplot as plt



HOST = '127.0.0.1'
PORT = 12000

#create my client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)


# To set waiting time of one second for reponse from server 
clientSocket.settimeout(1)

# Declare server's socket address
remoteAddr = ('Localhost', 12000)

arrayRTT = []
avgRTT = 0
minRTT = 10 # a big number
maxRTT = 0
count = 0
numOfPings = 10

# Ping ten times
for i in range(numOfPings):

    sendTime = time.time()
    message = 'ping ' + str(i + 1) + " " + str(time.strftime("%H:%M:%S"))
    clientSocket.sendto(message, remoteAddr)
    
    try:
        data, server = clientSocket.recvfrom(1024)
        recdTime = time.time()
        rtt = recdTime - sendTime
        if(rtt < minRTT) :
            minRTT = rtt
        if(rtt > maxRTT) :
            maxRTT = rtt
        avgRTT += rtt
        count += 1
        arrayRTT.append(rtt)
        print "Message Received", data
        print "Round Trip Time", rtt

        
        print
    
    except timeout:
        print 'REQUEST TIMED OUT'
        print

avgTotal = avgRTT / count  
print "Minimum Round Trip Time:", minRTT
print "Maximum Round Trip Time:", maxRTT
print "Average Round Trip Time:", avgTotal
print "Standard Deviation:", numpy.std(arrayRTT)
#print count, numOfPings
print "Packet Loss Rate:", float((numOfPings - count) * 10), "%"
plt.hist(arrayRTT, bins=[0,0.000625,0.00125,0.001875,0.0025,0.003125,0.00375,0.004375,0.005])