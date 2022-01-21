import sys
import os
os.chdir('D:\\华为云盘\\大师兄项目\\广州多边形\\案例\\鸿蒙python例程\\')
import machine
import time
machine.initBeep()
while True:
    machine.beep_on()
    time.sleep(1)
    machine.beep_off()
    time.sleep(1)
    print("11111")
    sys.stdout.flush()
