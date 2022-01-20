import oled
import time
oled.init()
a = 0
while a < 20:
    oled.showStr(0,0,"Count:" + str(a))
    a = a + 1
    time.sleep(1)
    oled.clear()
    time.sleep(1)
