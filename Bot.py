import Logic
import pyautogui
import time

WINDOW_SIZE = pyautogui.size()

COLUMNS = 15
LINES = 15
SCREEN_X_INIT = 0.439238653001 * WINDOW_SIZE[0]
SCREEN_Y_INIT = 0.259114583333 * WINDOW_SIZE[1]
SQUARE_EDGE = 19.9 * (WINDOW_SIZE[0] / WINDOW_SIZE[1])

answered_table = Logic.main(WINDOW_SIZE, SQUARE_EDGE)
print(answered_table)

pyautogui.hotkey('alt', 'tab')
time.sleep(0.1)

if COLUMNS == 15 and LINES == 15:
    x = SCREEN_X_INIT
    y = SCREEN_Y_INIT
    
    for line in range(LINES):
        for column in range(COLUMNS):
            if answered_table[line][column] == 1:
                pyautogui.moveTo(x, y)
                time.sleep(0.15)
                pyautogui.press('z')
            
            x += SQUARE_EDGE

        y += SQUARE_EDGE
        x = SCREEN_X_INIT