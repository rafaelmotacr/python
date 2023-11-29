import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 0.5
vezes = int(input("> Quantos personagens no total?: "))
link = str(input("> Mim dê o link papae: "))
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyperclip.copy(rf'{link}')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(6)
pyautogui.click(x = 356, y = 321)
pyautogui.scroll(-1380)
for personagem in range(1, vezes + 1):
    pyautogui.click(x = 356, y = 321)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.write(f'{personagem:0>2}')
    pyautogui.scroll(- 1360)
    