import machine
import time
machine.initBeep()
machine.initKey(9)
machine.initKey(10)
while True:
    if machine.getKey(9) == 0:
        machine.beep_on()
    if machine.getKey(10) == 0:
        machine.beep_off()
