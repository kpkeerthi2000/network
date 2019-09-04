import sys
import socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
while True:
        x, addr = s.recvfrom(1024)
        x=x.decode('utf-8')
        z=socket.gethostbyname(x)
        if(z==x):
                try:
                        zx=socket.gethostbyaddr(x)
                        print("Domain name is "+zx[0])
                except:
                        print("Unknown Host")
        else:
                try:
                        print("IP Address is "+z)
                except:
                        print("Unknown Host")
