# led灯例程：左右led灯交替点亮熄灭
import led
import time
# 初始化led灯（引脚分别为2和7）
led.init(2)
led.init(7)
while True:
    # 点亮引脚2的led灯
    led.on(2)
    # 熄灭引脚7的led灯
    led.off(7)
    time.sleep(1)
    # 熄灭引脚2的led灯
    led.off(2)
    # 点亮引脚7的led灯
    led.on(7)
    time.sleep(1)
