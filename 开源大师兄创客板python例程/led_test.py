import led
import time
led.init(2)
led.init(7)
while True:
    led.on(2)
    led.off(7)
    time.sleep(1)
    led.off(2)
    led.on(7)
    time.sleep(1)
