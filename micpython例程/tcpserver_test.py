# TCP服务端例程
import network
import socket
# 连接WiFi
network.connectWifi("POLYGON_ZONE","DB095438")
# 初始化TCP socket
soc = socket.socket()
# 绑定地址（IP和端口）
soc.bind(("0.0.0.0",12345))
# 监听连接
soc.listen(1)
# 接收连接
client = soc.accept()

while True:
    # 向客户端发送数据
    a = client.send("hello_world")
   
# 关闭socket
client.close()
soc.close()
