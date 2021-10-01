import pyautogui as df
import keyboard
import tty
import sys
import termios
import time

x = int(input('enter x position: '))
y = int(input('enter y position: '))

f = open('enterTheText.txt', 'r')
lines = f.readlines()

df.moveTo(x, y, duration=2)
df.click(x, y)
for line in lines:
    df.typewrite(line)
    time.sleep(0.5)
    df.typewrite(['enter'])