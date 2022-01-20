import network
import socket
import time
network.connectWifi("jdfxrobot","xiangjin")
soc = socket.socket()
soc.connect(("192.168.31.129",6000))
a = 10
while a > 0:
    soc.send("send + " + str(a))
    time.sleep(1)
    print(soc.recv())
    a = a - 1
soc.close()
