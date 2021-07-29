# _*_encoding:'utf-8' _*_
#鼠标相关操作
import pyautogui as gui
import time
import random

#KeyboardInterrupt 当一个当用户按下Ctrl+c的时候会触发的异常
try:
    while True:
        x , y = gui.position()
        print(x , y)
        time.sleep(0.3)
        # gui.moveTo(42, 444, duration=1)
except KeyboardInterrupt:
    print("\n程序运行结束")

#moveTo(x,y,duration = 1)
# gui.moveTo(42,444,duration = 1)#绝对移动
#鼠标自动点击
#gui.click(x,y)