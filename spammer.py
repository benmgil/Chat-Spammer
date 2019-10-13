#!/usr/bin/python
import pyautogui
import random
import time

delay = int(input("How many milliseconds do you want to wait in between each message?  "))
messages = open(input("What file with the messages do you want to open up?  ")).readlines()

input("Press Enter when your messaging app is loaded up.")
print("Click your mouse at the top left corner to toggle spamming.")
print("Press Ctrl-C in this window to stop.")
print("You have five seconds to refocus the text input area of your messaging app.")

time.sleep(5)

spam = True
pyautogui.FAILSAFE = False

while True:         #Message sending loop
	if pyautogui.position()[0] < 50 and pyautogui.position()[1] < 50:
		while pyautogui.position()[0] < 50 and pyautogui.position()[1] < 50:
			pass
		spam = False
	
	if spam:
		pyautogui.typewrite(random.choice(messages))     
		pyautogui.press("enter")

	time.sleep(delay/1000)


print("Done\n")
