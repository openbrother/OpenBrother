import network
import socket
network.connectWifi("POLYGON_ZONE","DB095438")
soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soc.bind(("0.0.0.0",12345))
a = 10
while a > 0:
    soc.sendto("send" + str(a),("192.168.0.105",12345))
    print(soc.recvfrom(128))
soc.close()
