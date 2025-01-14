import Logic
import pyautogui
import time

COLUMNS = 15
LINES = 15
SCREEN_X_INIT = 600
SCREEN_Y_INIT = 199
SQUARE_EDGE = 35

answered_table = Logic.main()

pyautogui.hotkey('alt', 'tab')
time.sleep(0.1)

if COLUMNS == 15 and LINES == 15:
    x = SCREEN_X_INIT
    y = SCREEN_Y_INIT
    
    for line in range(LINES):
        for column in range(COLUMNS):
            if answered_table[line][column] == 1:
                print(f'line: {line} column: {column}')
                pyautogui.moveTo(x, y)
                time.sleep(0.15)
                pyautogui.press('z')
            
            x += SQUARE_EDGE

        y += SQUARE_EDGE
        x = SCREEN_X_INIT