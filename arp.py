import socket
from binascii import hexlify

def proper_mac(MAC_Addr):
	mac = ""
	count = 0
	for i in range(len(MAC_Addr)):
		mac = mac + chr(MAC_Addr[i])
		count=count+1
		if(count==2):
			count=0
			mac=mac+':'
	return mac


def get_MAC_Addr(interface,port=0):
    s=socket.socket(socket.AF_PACKET,socket.SOCK_RAW)
    s.bind((interface,port))
    mac=hexlify(s.getsockname()[4])
    s.close()
    return proper_mac(mac)

print("MAC Address is:",get_MAC_Addr("enp0s20f0u1"))
