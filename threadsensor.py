import socket
import logging
import threading
import time
import socket



def discovery(UDPServerSocket):
    # print(UDPServerSocket) 
    bytesToSend = str.encode("discovery")
    routerAddressPort = ("127.0.0.1", 20007)
    UDPServerSocket.sendto(bytesToSend,routerAddressPort)


def pi_sensor(i):
    localIP = "127.0.0.1"
    localPort = i
    bufferSize = 1024
    msgFromSensor = "Hello UDP Client from Port: " + str(i)
    bytesToSend = str.encode(msgFromSensor)
    UDPServerSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP,localPort))
    print("UDP snsor up and listening in port "+str(i))
    discovery(UDPServerSocket)
    while(True):
        bytesAddressPair=UDPServerSocket.recvfrom(bufferSize)
        message=bytesAddressPair[0]
        address=bytesAddressPair[1]
        clientMsg="MessagefromClient:{}".format(message)
        clientIP="ClientIPAddress:{}".format(address)
        print(clientMsg)
        print(clientIP)
        UDPServerSocket.sendto(bytesToSend,address)

for i in [20001,20002,20003,20005,20006]:
    logging.info("Main    : create and start thread %d.", i)
    x = threading.Thread(target=pi_sensor, args=(i,))
    x.start()
    time.sleep(4)
    