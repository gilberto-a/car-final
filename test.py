import keyboard
import time


time.sleep(5)
for i in range(20):
    keyboard.press('a')
    time.sleep(0.1)
keyboard.release('a')