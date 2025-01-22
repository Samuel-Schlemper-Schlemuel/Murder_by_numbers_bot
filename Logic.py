from picross_solver import picross_solver
import analize_print
import numpy as np

actual_parameter = 0
parameters = [
    {'background_color': 230, 'thresh': 70, 'standart_box_size': 90},
    {'background_color': 240, 'thresh': 90, 'standart_box_size': 90},
    {'background_color': 255, 'thresh': 70, 'standart_box_size': 70},
    {'background_color': 240, 'thresh': 65, 'standart_box_size': 75}
]

def main(window_size: tuple, square_edge: float, num_of_columns: int, num_of_lines: int):
    global actual_parameter

    try:
        init_column_y_constant = 0.013020833
        init_column_x_constant = 0.428257687
        init_line_y_constant = 0.240885417
        init_line_x_constant = 0.300146413

        if num_of_columns == 20 and num_of_lines == 15:
            init_column_y_constant = 0.097222222
            init_line_y_constant = 0.330555556

        if num_of_columns == 15 and num_of_lines == 10:
            init_column_y_constant = 0.127777778
            init_line_y_constant = 0.358333333

        data = analize_print.main(
            image_path = './screenshot.png',
            tesseract_path = r'/bin/tesseract',
            init_column_y = init_column_y_constant * window_size[1],
            init_column_x = init_column_x_constant * window_size[0],
            init_line_y = init_line_y_constant * window_size[1],
            init_line_x = init_line_x_constant * window_size[0],
            square_edge = square_edge,
            window_size = window_size,
            num_of_columns = num_of_columns,
            num_of_lines = num_of_lines,
            parameters = parameters[actual_parameter]
        )

        rows = data['rows']
        columns = data['cols']

        puzz = np.full((num_of_lines, num_of_columns), -1)

        picross_solver.solve(rows, columns, puzz)
    except:
        actual_parameter += 1

        if actual_parameter < len(parameters):
            puzz = main(window_size, square_edge, num_of_columns, num_of_lines)

    worked = True

    for line in range(len(puzz)):
        for column in range(len(puzz[line])):
            if puzz[line][column] == -1:
                worked = False
                break

        if not worked:
            break

    if not worked:
        actual_parameter += 1

        if actual_parameter < len(parameters):
            puzz = main(window_size, square_edge, num_of_columns, num_of_lines)
    else:
        print(f'columns: {data["cols"]}')
        print(f'rows: {data["rows"]}')
        print(parameters[actual_parameter])

    return puzz

if __name__ == '__main__':
    import pyautogui
    COLUMNS = int(input('columns: '))
    LINES = int(input('lines: '))

    WINDOW_SIZE = pyautogui.size()
    SQUARE_EDGE = 28 * (WINDOW_SIZE[0] / WINDOW_SIZE[1]) * (15/(COLUMNS if COLUMNS > LINES else LINES))
    solution = main(WINDOW_SIZE, SQUARE_EDGE, COLUMNS, LINES)

    for line in solution:
        print(line)