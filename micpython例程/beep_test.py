# 蜂鸣器例程：蜂鸣器重复打开关闭
import machine
import time
# 初始化蜂鸣器
machine.initBeep()
while True:
    # 打开蜂鸣器
    machine.beep_on()
    time.sleep(1)
    # 关闭蜂鸣器
    machine.beep_off()
    time.sleep(1)
