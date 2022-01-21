# 按键例程：按下引脚9按键打开蜂鸣器，按下引脚10按键关闭蜂鸣器
import machine
import time
# 初始化蜂鸣器
machine.initBeep()
# 初始化按键（引脚9）
machine.initKey(9)
# 初始化按键（引脚10）
machine.initKey(10)
while True:
    # 获取按键状态（引脚9），返回0代表按下按键
    if machine.getKey(9) == 0:
        #消抖
        while machine.getKey(9) == 0:
            pass
        machine.beep_on()
    # 获取按键状态（引脚10），返回0代表按下按键
    if machine.getKey(10) == 0:
        #消抖
        while machine.getKey(10) == 0:
            pass
        machine.beep_off()
