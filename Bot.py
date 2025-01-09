import Logic
import pyautogui
import time

COLUMNS = 15
LINES = 15
SQUARE_EDGE = 50

answered_table = Logic.main()

for line in answered_table:
    print(line)

pyautogui.hotkey('alt', 'tab')
time.sleep(0.1)

if COLUMNS == 15 and LINES == 15:
    x = 850
    y = 282
    
    for line in range(LINES):
        for column in range(COLUMNS):
            if answered_table[line][column] == '█':
                pyautogui.moveTo(x, y)
                time.sleep(0.15)
                pyautogui.press('z')
            
            x += SQUARE_EDGE

        y += SQUARE_EDGE
        x = 850