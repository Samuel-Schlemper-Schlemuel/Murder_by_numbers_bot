from picross_solver import picross_solver
import analize_print
import numpy as np

def main(window_size: tuple, square_edge: float, num_of_columns: int, num_of_lines: int):
    data = analize_print.main(
        image_path = './screenshot.png',
        tesseract_path = r'/bin/tesseract',
        init_column_y = 0.013020833 * window_size[1],
        init_column_x = 0.428257687 * window_size[0],
        init_line_y = 0.240885417 * window_size[1],
        init_line_x = 0.300146413 * window_size[0],
        square_edge = square_edge,
        window_size = window_size,
        num_of_columns = num_of_columns,
        num_of_lines = num_of_lines
    )

    print(data)

    rows = data['rows']
    columns = data['cols']

    puzz = np.full((15, 15), -1)

    picross_solver.solve(rows, columns, puzz)

    return puzz

if __name__ == '__main__':
    import pyautogui

    WINDOW_SIZE = pyautogui.size()
    SQUARE_EDGE = 28 * (WINDOW_SIZE[0] / WINDOW_SIZE[1])
    solution = main(WINDOW_SIZE, SQUARE_EDGE)

    for line in solution:
        print(line)