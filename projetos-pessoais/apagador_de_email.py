import pyautogui;
import pyperclip;
from time import sleep

pyautogui.PAUSE = 1;

pyautogui.press('win');
pyautogui.write('chrome');
pyautogui.press('enter');
pyautogui.hotkey('ctrl', 't');
pyautogui.write(r'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox');
pyautogui.press('enter');
sleep(5)
pyautogui.click(y = 140, x = 357);
pyautogui.write("from:noreply@youtube.com")
pyautogui.press('enter')
sleep(2)
while True:
    pyautogui.click(y = 250, x = 283);
    pyautogui.click(y = 237, x = 429);
    sleep(2.5)

