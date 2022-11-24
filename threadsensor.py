import logging
import threading
import time
import socket


def pi_sensor(i):
    message = "Hello UDP Server "+str(i)
    send = str.encode(message)
    server_address = ("127.0.0.1", i)
    buffer_size = 1024
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.sendto(send, server_address)
    msgFromServer = UDPClientSocket.recvfrom(buffer_size)
    message=msgFromServer[0]
    address=msgFromServer[1]
    server_Msg="Message from Server:{}".format(message)
    serverIP="Server IP Address:{}".format(address)
    print(server_Msg)
    print(serverIP)

for i in [20001,20002,20003,20004,20005,20006]:
    logging.info("Main    : create and start thread %d.", i)
    x = threading.Thread(target=pi_sensor, args=(i,))
    x.start()
    time.sleep(4)