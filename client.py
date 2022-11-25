import socket

message = "temperature/pressure"
send = str.encode(message)
server_address = ("127.0.0.1", 20002)
buffer_size = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(send, server_address)
msgFromServer = UDPClientSocket.recvfrom(buffer_size)
message=msgFromServer[0]
address=msgFromServer[1]
server_Msg=message.decode()
serverIP="Server IP Address : {}".format(address)
print(server_Msg)
print(serverIP)