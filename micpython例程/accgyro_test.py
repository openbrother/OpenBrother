import oled
import machine
import time
oled.init()
machine.initBeep()
machine.icm_init()
a = 0
while True:
    acc = machine.read_acc()
    oled.showStr(0,0,"Count:" + str(acc))
    time.sleep(1)
    oled.clear()
