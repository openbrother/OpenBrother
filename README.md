# OpenBrother青少年开源教育项目

## 介绍
**“开源大师兄”开源教育项目是由一线608位老师共同发起的开源教育项目**
项目的目的是为了解决我国青少年开源教育的软硬件、课程、平台的自主可控性，目前项目包括“开源大师兄”硬件项目，“开源大师兄”软件项目、“开源大师兄”课程项目。官网地址：

 [https://www.openbrother.com](https://www.openbrother.com)

## "开源大师兄"创客板

### 1.硬件开源资料及代码示例

https://gitee.com/hihopeorg_group/hi-hope-k-board


### 2.固件升级方法

​	1.请下载固件及固件升级软件，下载地址：https://www.aliyundrive.com/s/KUVgHn52B2d 

​	2.按照说明文档进行升级，具体说明文档请参考下载地址内的固件说明。

### 3.软件下载地址及使用说明

1.  下载地址：https://www.aliyundrive.com/s/KUVgHn52B2d
2.  下载安装完后，请升级软件为最新版本。
3.  参考下载地址内的说明文档进行相关操作。

### 4.大师兄创客板Python-machine库说明

#### 按键、蜂鸣器、陀螺仪加速度相关库

使用前先import machine

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

#### led库：

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

#### oled库：

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

#### 文件系统：

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
