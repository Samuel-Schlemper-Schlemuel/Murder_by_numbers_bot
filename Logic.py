import numpy as np

# c --> Column
# l --> Line

table = {
    'c0': '6',
    'c1': '2 1 2 1',
    'c2': '1 1 5 2',
    'c3': '2 2 3 3',
    'c4': '2 1 5 2',
    'c5': '2 1 1 1',
    'c6': '1 1 1 4',
    'c7': '12',
    'c8': '3 8',
    'c9': '3 2 3',
    'c10': '1 2 2',
    'c11': '1 1 5', 
    'c12': '2 3 2',
    'c13': '2 3 2',
    'c14': '1 1 4',
    'l0': '5 4',
    'l1': '2 5 2',
    'l2': '1 1 2',
    'l3': '2 6 1',
    'l4': '1 2 3',
    'l5': '1 1 4 1',
    'l6': '3 1 3',
    'l7': '4 3',
    'l8': '3 8',
    'l9': '7 3',
    'l10': '3 5',
    'l11': '2 2 1',
    'l12': '3 3 1 2',
    'l13': '3 6',
    'l14': '2 4',
}


# Used by other Functions


def getting_the_max_between_lines_and_columns(LINES, COLUMNS):
    line_sum = 0
    column_sum = 0

    for column in range(COLUMNS):
        actual_column_list = table[f'c{column}'].split(' ')
        
        for num in actual_column_list:
            column_sum += int(num)

    for line in range(LINES):
        actual_column_list = table[f'l{line}'].split(' ')
        
        for num in actual_column_list:
            line_sum += int(num)

    if column_sum > line_sum:
        return 'column'
    else:
        return 'line'


def all_1_in_sequence(sequence: object):
    all_1_sequences = list()
    repeated_1 = 0

    for i in range(len(sequence)):
        if sequence[i] == 1:
            repeated_1 += 1
        elif repeated_1 >= 1:
            all_1_sequences.append(repeated_1)
            repeated_1 = 0

    return all_1_sequences


# Usend by the Main function


def next_possibility(LINES, COLUMNS, result):
    pass


def finished(LINES, COLUMNS, result, bigger_betwenn_lines_and_columns):
    seeing = None
    letter = None
    seeing_range = None

    if bigger_betwenn_lines_and_columns == 'column':
        seeing = 'lines'
        letter = 'l'
        seeing_range = LINES
    else:
        seeing = 'columns'
        letter = 'c'
        seeing_range = COLUMNS
    
    for position in range(seeing_range):
        sequence_string = table[f'{letter}{position}']
        sequence_list = None

        if seeing == 'lines':
            sequence_list = result[position]
        else:
            sequence_list = result[0:LINES, position]

        all_ones = all_1_in_sequence(sequence_list)

        if len(sequence_string) != len(all_ones):
            return False
        else:
            for i in range(len(sequence_string)):
                if int(sequence_string[i]) != all_ones[i]:
                    return False
                
    return True




def main(LINES: int, COLUMNS: int):
    result = np.zeros((LINES, COLUMNS))
    count = 0

    bigger_betwenn_lines_and_columns = getting_the_max_between_lines_and_columns(LINES, COLUMNS)

    while True:
        past_result = result.copy()
        result = next_possibility(LINES, COLUMNS, result)

        if finished(LINES, COLUMNS, result, bigger_betwenn_lines_and_columns):
            count += 1
            print(f'The algorithm complete the puzzle in {count} loops')
            break
        elif np.array_equal(past_result, result):
            print(f'The algorithm was unable to complete the puzzle in {count} loops')
            break

        count += 1

    return result

if __name__ == '__main__':
    print(main(15, 15))