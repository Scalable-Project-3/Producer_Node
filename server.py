import socket
import logging
import threading
import time
import socket
import random

def sensorData(clientMsg):
    sensorValue = ""
    if "temperature" in clientMsg:
        sensorValue = "Temperature : "+str(random.randint(40, 90))
    elif "pressure" in clientMsg:
        sensorValue = "Pressure : "+str(random.randint(40, 90))
    elif "speed" in clientMsg:
        sensorValue = "Speed : "+str(random.randint(40, 90))
    elif "surroundingtemperature" in clientMsg:
        sensorValue = "Surrounding Temperature : "+str(random.randint(40, 90))
    elif "bloodoxygenlevel" in clientMsg:
        sensorValue = "Blood oxygen level : "+str(random.randint(40, 90))
    elif "heartbeat" in clientMsg:
        sensorValue = "Heart Beat : "+str(random.randint(40, 90))
    elif "hydration" in clientMsg:
        sensorValue = "Hydration : "+str(random.randint(40, 90))
    elif "bloodsugar" in clientMsg:
        sensorValue = "Blood Sugar "+str(random.randint(40, 90))

    return sensorValue


localIP = "127.0.0.1"
localPort = 20007
bufferSize = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)
UDPServerSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP,localPort))
print("UDP server up and listening")
while(True):
    bytesAddressPair=UDPServerSocket.recvfrom(bufferSize)
    message=bytesAddressPair[0]
    address=bytesAddressPair[1]
    clientMsg = message.decode("utf-8")
    clientIP="ClientIPAddress:{}".format(address)
    # print(clientMsg)
    # print(clientIP)
    msgFromServer = sensorData(clientMsg)
    bytesToSend = str.encode(msgFromServer)
    UDPServerSocket.sendto(bytesToSend,address)