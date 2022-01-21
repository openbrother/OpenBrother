# 开源大师兄创客板machine库说明

（版本号：2022.1.21）

### machine库说明：

按键、蜂鸣器、陀螺仪加速度相关库，使用前先import machine
（两个按键引脚分别是9和10）

##### 1.machine.initKey(pin)

参数pin: 按键对应引脚
初始化按键 

##### 2.machine.getKey(pin)

参数pin: 按键对应引脚
获取按键当前状态（是否按下）

##### 3.machine.initBeep()

初始化蜂鸣器

##### 4.machine.beep_on()

打开蜂鸣器

##### 5.machine.beep_off()

关闭蜂鸣器

##### 6.machine.read_gyro()

读取陀螺仪三轴数据，返回包含XYZ三轴数据的元组

##### 7.machine.read_acc()

读取加速度计三轴数据，返回包含XYZ三轴数据的元组

### led库：

两盏led灯使用库，使用前先import led
（两个led灯引脚分别是2和7）

##### 1.led.init(pin)

参数pin: led灯对应引脚
初始化led灯

##### 2.led.on(pin)

参数pin: led灯对应引脚
点亮led灯

##### 3.led.off(pin)

参数pin: led灯对应引脚
熄灭led灯

### oled库：

显示屏使用库，使用前先import oled

##### 1.oled.init()

初始化显示屏

##### 2.oled.showStr(x,y,content)

参数x:内容显示的行数
参数y:内容显示的列数
参数content:要显示的字符(暂不支持中文)
在显示屏指定位置显示字符

##### 3.oled.clear()

清空显示屏

### 文件系统：

文件库

##### 1.open(filename,mode)

参数filename:要打开的文件名
参数mode:打开文件的模式(“w”:写入模式; “w+”:写入模式，若文件不存在则新建文件; “r”:读取模式;)
打开文件，返回文件对象

##### 2.file.write(content)

参数content:要写入的文件内容
写入内容到文件

##### 3.file.read([n])

可选参数n:要读取内容的长度
读取文件，返回字符串

##### 4.file.close()

关闭文件

### network库

网络使用库，用于连接wifi或启动热点，使用前先import network

##### 1.network.connectWifi(ssid, password)

参数ssid：要连接的WiFi名
参数password：要连接的WiFi的密码
连接WiFi

##### 2.network.disconnectWifi()

断开WiFi连接

##### 3.network.startHotspot(ssid, password)

参数ssid：创建的WiFi名
参数password：创建的WiFi密码
创建WiFi热点

##### 4.network.stopHotspot()

关闭WiFi热点

### socket库

socket使用库，用于网络socket通信，使用前先import socket

##### 1.socket.socket([family,sockettype])

可选参数family：IP协议类型，填socket.AF_INET/socket.AF_INET6分表代表IPv4/ IPv6类型的socket
可选参数sockettype：socket类型，填socket.SOCK_STREAM/socket.SOCK_DGRAM分表代表TCP/UDP类型的socket
初始化socket，不填参数默认为IPv4协议的TCP的socket

##### 2.my_socket.connect(address)

参数address：服务器地址
连接服务器，如 my_socket.connect ((“192.168.0.1”, 8888))

##### 3.my_socket.send(content)

参数content：要发送的内容（字符串）
socket发送数据

##### 4.my_socket.recv()

socket接收数据，返回收到的数据（字符串）

##### 5.my_socket.bind(address)

参数address：要绑定的地址
绑定socket地址，如 my_socket.bind ((“192.168.0.1”, 8888))
，地址里的ip一般直接用“0.0.0.0”即可

##### 6.my_socket.listen(num)

参数num：监听连接数量
开始监听socket

##### 7.my_socket.accept()

socket接收连接

##### 8.my_socket.sendto(content, address)

参数content：要发送的内容（字符串）
参数address：要发送数据的目标地址
socket发送UDP数据

##### 9.my_socket.recvfrom(n)

参数n：接收数据长度
socket接收UDP数据

##### 10.my_socket.close()

关闭socket

### thread库

多线程库，使用前先import _thread_

##### 1.thread.start_new_thread(func,params)

参数func：新线程传入的函数名
参数params：新线程函数的参数列表（类型为元组）
启动新线程

### time库

时间库，使用前先import time

##### 1．time.sleep(seconds)

参数seconds：休眠时间（秒）
休眠

##### 2．time.msleep(mseconds)

参数mseconds：休眠时间（毫秒）
休眠

##### 3．time.usleep(useconds)

参数useconds：休眠时间（微秒）
休眠

##### 4．time.tick_ms()

获取系统时间戳（毫秒）