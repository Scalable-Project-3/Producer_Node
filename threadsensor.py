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

def discovery(UDPsensor):
    # print(UDPsensor) 
    bytesToSend = str.encode("discovery")
    routerAddressPort = ("127.0.0.1", 20007)
    UDPsensor.sendto(bytesToSend,routerAddressPort)


def pi_sensor(i):
    localIP = "127.0.0.1"
    localPort = i[0]
    bufferSize = 1024
    UDPsensor=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    UDPsensor.bind((localIP,localPort))
    print("UDP snsor up and listening in port "+str(i[0]))
    discovery(UDPsensor)
    while(True):
        bytesAddressPair=UDPsensor.recvfrom(bufferSize)
        message=bytesAddressPair[0]
        address=bytesAddressPair[1]
        clientMsg = message.decode("utf-8")
        msgFromServer = i[1]+"\n"+sensorData(clientMsg)
        bytesToSend = str.encode(msgFromServer)
        UDPsensor.sendto(bytesToSend,address)

for i in [[20001,'Bob'],[20002,'Alice'],[20003,'Eve'],[20005,'John'],[20006,'Ben']]:
    logging.info("Main    : create and start thread %d.", i)
    x = threading.Thread(target=pi_sensor, args=(i,))
    x.start()
    time.sleep(4)
    