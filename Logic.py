import json
from nonogram_cracker import solve

def main():
    # Example usage
    table = {
        'c0': '1 2 2 1',
        'c1': '2 1 1 2',
        'c2': '1 2 2 1',
        'c3': '1 1 6',
        'c4': '3 1',
        'c5': '1 4',
        'c6': '5',
        'c7': '1 3 2',
        'c8': '1 1 4 1 1 1',
        'c9': '1 3 1 1',
        'c10': '2 3 1 1 1 1',
        'c11': '1 3 1 2',
        'c12': '1 2 1 1 1 1',
        'c13': '2 1 1 1 2',
        'c14': '1 1 1 1 1',
        'l0': '4 4',
        'l1': '2 2 4',
        'l2': '3 1 2',
        'l3': '3 1 1',
        'l4': '1 1 1 1',
        'l5': '1 1',
        'l6': '1 2',
        'l7': '1 1 2',
        'l8': '3 3 2',
        'l9': '3 3 2',
        'l10': '1 3 2 2',
        'l11': '1 4 2',
        'l12': '1 2 2 2',
        'l13': '2 1 4 3',
        'l14': '3 2 3',
    }

    rows = []
    colums = []

    for key, value in table.items():
        if key.startswith('c'):
            colums.append([int(number) for number in value.split(' ')])
        else:
            rows.append([int(number) for number in value.split(' ')])

    solution = solve({
    "name": "test",
    "rows": rows,
    "cols": colums
    })

    return solution['solution']

if __name__ == '__main__':
    solution = main()

    for line in solution:
        print(line)