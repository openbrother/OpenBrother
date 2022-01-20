import oled
import machine
import time
oled.init()
machine.initBeep()
machine.icm_init()
a = 0
while True:
    gyro = machine.read_gyro()
    oled.showStr(0,0,"Count:" + str(gyro))
    time.sleep(1)
    oled.clear()
