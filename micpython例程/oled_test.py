# oled显示屏例程：显示屏计数
import oled
import time
# 初始化显示屏
oled.init()
a = 0
while True:
    # 在显示屏的0行0列显示字符串
    oled.showStr(0,0,"Count:" + str(a))
    a = a + 1
    time.sleep(1)
    # 显示屏清屏
    oled.clear()
    time.sleep(1)
