# _*_encoding:'utf-8' _*_
#屏幕坐标
import pyautogui as gui
from PIL import Image
import time
try:
    while True:
        x , y = gui.position()
        image = gui.screenshot()
        t = image.getpixel((x , y))
        print(str(x).rjust(4) , str(y).rjust(4) , str(t[0]).rjust(4), str(t[1]).rjust(4), str(t[2]).rjust(4))
        time.sleep(0.3)

except KeyboardInterrupt:
    print("停止")