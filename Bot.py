import Logic
import pyautogui
import time

COLUMNS = 15
LINES = 15
SQUARE_EDGE = 50

answered_table = Logic.main(COLUMNS, LINES)

print(answered_table)

pyautogui.hotkey('alt', 'tab')

if COLUMNS == 15 and LINES == 15:
    x = 850
    y = 282
    
    for line in range(LINES):
        for column in range(COLUMNS):
            if answered_table[line][column] == 1:
                pyautogui.moveTo(x, y)
                time.sleep(0.2)
                pyautogui.press('z')
            elif answered_table[line][column] == -1:
                pyautogui.moveTo(x, y)
                time.sleep(0.2)
                pyautogui.press('x')
            
            x += SQUARE_EDGE

        y += SQUARE_EDGE
        x = 850