import socket

message = "bob/temperature"
send = str.encode(message)
server_address = ("127.0.0.1", 20007)
buffer_size = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(send, server_address)
msgFromServer = UDPClientSocket.recvfrom(buffer_size)
message=msgFromServer[0]
address=msgFromServer[1]
server_Msg="Message from Server : {}".format(message)
serverIP="Server IP Address : {}".format(address)
print(server_Msg)
print(serverIP)