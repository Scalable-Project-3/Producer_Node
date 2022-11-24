import socket

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
    clientMsg="MessagefromClient:{}".format(message.decode("utf-8"))
    clientIP="ClientIPAddress:{}".format(address)
    print(clientMsg)
    print(clientIP)
    # UDPServerSocket.sendto(bytesToSend,address)