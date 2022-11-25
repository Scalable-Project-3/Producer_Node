import socket
import logging
import threading
import time
import socket
import random

def sensorData(clientMsg):
    clientMsg = clientMsg.lower()
    clientMsg = clientMsg.replace(" ","")
    clientMsg = clientMsg.split('/') 
    sensorValue = ""
    if "temperature" in clientMsg:
        sensorValue += "Temperature : "+str(random.randint(35, 40)) +"\n"
    if "pressure" in clientMsg:
        sensorValue += "Pressure : "+str(random.randint(76, 84))+"\n"
    if "speed" in clientMsg:
        sensorValue += "Speed : "+str(random.randint(0, 5))+"\n"
    if "surroundingtemperature" in clientMsg:
        sensorValue += "Surrounding Temperature : "+str(random.randint(5, 10))+"\n"
    if "bloodoxygenlevel" in clientMsg:
        sensorValue += "Blood oxygen level : "+str(random.randint(80, 100))+"\n"
    if "heartbeat" in clientMsg:
        sensorValue += "Heart Beat : "+str(random.randint(75, 80))+"\n"
    if "hydration" in clientMsg:
        sensorValue += "Hydration : "+str(random.randint(69, 73))+"\n"
    if "bloodsugar" in clientMsg:
        sensorValue += "Blood Sugar "+str(random.randint(89, 93))+"\n"

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
    print(clientMsg)
    print(clientIP)
    msgFromServer = sensorData(clientMsg)
    bytesToSend = str.encode(msgFromServer)
    # UDPServerSocket.sendto(bytesToSend,address)