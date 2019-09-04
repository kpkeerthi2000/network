import socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 8080
host = (UDP_IP_ADDRESS,UDP_PORT_NO)
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while(1):
        x=input("Enter domain name: ")
        clientSock.sendto(x.encode('utf-8'), host)
