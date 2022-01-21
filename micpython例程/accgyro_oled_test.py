# 传感器例程：读取加速度计和陀螺仪数据并在LCD上显示
import machine
import oled
import time
# 硬件初始化
machine.icm_init()
# 初始化显示屏
oled.init()
while True: 
    acc = machine.read_acc()
    # 读取陀螺仪数据，返回三元元组
    gyro = machine.read_gyro()
    # 在显示屏的0列0行显示字符串
    oled.showStr(0,0,str(acc))
    # 在显示屏的0列4行显示字符串 
    oled.showStr(0,4,str(gyro))
    time.sleep(1)
    oled.clear()
   
    
   
    
 
    
