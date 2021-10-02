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
text = ''
for line in lines:
    text += line

df.moveTo(x, y, duration=2)
df.click(x, y)
for character in text:
    df.write(character)