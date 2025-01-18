from picross_solver import picross_solver
import analize_print
import numpy as np

def main(window_size: tuple, square_edge: float):
    data = analize_print.main(
        image_path = '/home/schlemuel/Imagens/Capturas de tela/Captura de tela de 2025-01-18 12-40-09.png',
        tesseract_path = r'/bin/tesseract',
        init_column_y = 0.013020833 * window_size[1],
        init_column_x = 0.428257687 * window_size[0],
        init_line_y = 0.240885417 * window_size[1],
        init_line_x = 0.300146413 * window_size[0],
        square_edge = square_edge,
        window_size = window_size
    )

    rows = data['rows']
    columns = data['cols']

    print(f'rows: {rows}')
    print(f'columns: {columns}')
    
    puzz = np.full((15, 15), -1)

    picross_solver.solve(rows, columns, puzz)

    return puzz

if __name__ == '__main__':
    import pyautogui

    WINDOW_SIZE = pyautogui.size()
    SQUARE_EDGE = 19.9 * (WINDOW_SIZE[0] / WINDOW_SIZE[1])
    solution = main(WINDOW_SIZE, SQUARE_EDGE)

    for line in solution:
        print(line)