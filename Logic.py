import json
from picross_solver import picross_solver
import analize_print
import numpy as np

def main():
    data = analize_print.main(
        image_path = '/home/schlemuel/Imagens/Capturas de tela/Captura de tela de 2025-01-09 15-12-32.png',
        tesseract_path = r'/bin/tesseract',
        init_column_y = 20,
        init_column_x = 822,
        init_line_y = 260,
        init_line_x = 585
    )

    rows = data['rows']
    columns = data['cols']
    puzz = np.full((15, 15), -1)

    solution = picross_solver.solve(rows, columns, puzz)

    return puzz

if __name__ == '__main__':
    solution = main()

    for line in solution:
        print(line)