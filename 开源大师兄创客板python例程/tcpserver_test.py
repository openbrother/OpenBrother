import network
import socket
network.connectWifi("POLYGON_ZONE","DB095438")
soc = socket.socket()
soc.bind(("0.0.0.0",12345))
soc.listen(1)
client = soc.accept()
a = 10
b = 0
while a > 0:
    client.send(client.recv())
client.close()
soc.close()
