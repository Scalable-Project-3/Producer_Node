import socket

msg = "Hello this Jimmy"
bytesToSend = str.encode(msg)
serverAddressPort = ("127.0.0.1", 20007)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.bind(serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
message=msgFromServer[0]
address=msgFromServer[1]
serverMsg="Message from Server:{}".format(message)
serverIP="Server IP Address:{}".format(address)
print(serverMsg)
print(serverIP)