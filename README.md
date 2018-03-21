# Chat Spammer

## Disclaimer
Sending too many messages to others at once can crash recipients devices. I am not responsible for how you use this software. This is for educational purposes only. Now that that's out of the way...

## About
This project is a simple python script that simulates keyboard presses to spam repeated messages through any message-sending computer application.
It allows you to define a message to send or to send the contents of your computer's clipboard, as well as a number of times to send the message and how long to wait in between each one.

## Install it
To run the bot, you must have Python installed, as well as the pyautogui library. You can install that dependency with
```
pip install pyautogui
```
## Run it
After that just navigate to the directory where you saved the script and run it, it will prompt you for the rest of the information.
```
python spammer.py
```
It will prompt you to open your messaging app and focus the textbox where messages are inputted, and to press Enter when you are ready to begin. Once you press enter, you will have a few seconds to refocus the textbox before the bot will begin typing.

