import Logic
import pyautogui
import time
import os

try:
    print('Wait the code finish before use the computer again')
    WINDOW_SIZE = pyautogui.size()
    COLUMNS = int(input("Number of columns: "))
    LINES = int(input("Number of lines: "))
    SQUARE_EDGE = 28 * (WINDOW_SIZE[0] / WINDOW_SIZE[1]) * (15/(COLUMNS if COLUMNS > LINES else LINES))

    time.sleep(0.2)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)

    try:
        os.remove('./screenshot.png')
    except:
        pass

    pyautogui.screenshot('screenshot.png')

    answered_table = Logic.main(WINDOW_SIZE, SQUARE_EDGE, COLUMNS, LINES)
    print(answered_table)

    SCREEN_BOX_X_INIT = 0.439238653001 * WINDOW_SIZE[0]
    SCREEN_BOX_Y_INIT = 0.259114583333 * WINDOW_SIZE[1]

    if COLUMNS == 20 and LINES == 15:
        SCREEN_BOX_Y_INIT = 0.342592593 * WINDOW_SIZE[1]
    elif COLUMNS == 15 and LINES == 10:
        SCREEN_BOX_Y_INIT = 0.373148148 * WINDOW_SIZE[1]

    x = SCREEN_BOX_X_INIT
    y = SCREEN_BOX_Y_INIT
    
    for line in range(LINES):
        for column in range(COLUMNS):
            if answered_table[line][column] == 1:
                pyautogui.moveTo(x, y)
                time.sleep(0.15)
                pyautogui.press('z')
            
            x += SQUARE_EDGE

        y += SQUARE_EDGE
        x = SCREEN_BOX_X_INIT

except:
    pyautogui.alert(text='Some error occurred')