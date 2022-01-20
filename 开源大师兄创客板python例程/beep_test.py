import machine
import time
machine.initBeep()
a = 0
while a< 20:
    machine.beep_on()
    time.sleep(1)
    machine.beep_off()
    time.sleep(1)
    print("11111")
    a+=1
