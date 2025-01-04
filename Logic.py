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


def bigger(sequence: str):
    sequence_split = sequence.split(' ')

    bigger_and_second_bigger = {
        'First': False,
        'Last': False,
        'num_bigger': 0,
        'position_bigger': -1,
        'num_second_bigger': -1
    }

    for i in range(len(sequence_split)):
        value = int(sequence_split[i])

        if value > bigger_and_second_bigger['num_bigger']:
            bigger_and_second_bigger['num_second_bigger'] =  bigger_and_second_bigger['num_bigger']
            bigger_and_second_bigger['num_bigger'] =  value
            bigger_and_second_bigger['position_bigger'] = i
        elif value == bigger_and_second_bigger['num_bigger']:
            bigger_and_second_bigger['position_bigger'] = -1
            bigger_and_second_bigger['num_second_bigger'] =  bigger_and_second_bigger['num_bigger']
        elif value > bigger_and_second_bigger['num_second_bigger']:
            bigger_and_second_bigger['num_second_bigger'] = value

    if bigger_and_second_bigger['position_bigger'] == 0:
        bigger_and_second_bigger['First'] = True

    if bigger_and_second_bigger['position_bigger'] == (len(sequence_split) - 1):
        bigger_and_second_bigger['Last'] = True

    return bigger_and_second_bigger
    

def see_1_in_sequence(sequence: object):
    result = {
        'max_num': 0,
        'actual': 0,
        'last_1_position': -1,
        'first_1_position': -1,
        'first_max_1_position': -1,
        'last_max_1_position': -1,
        'actual_1_position': -1
    }

    for i in range(len(sequence)):
        number = sequence[i]

        if number == 1:
            if result['first_1_position'] == -1:
                result['first_1_position'] = i

            result['actual'] += 1
            result['actual_1_position'] = i

            if result['actual'] > result['max_num']:
                result['max_num'] = result['actual']
                result['last_max_1_position'] = i

            result['last_1_position'] = i

        else:
            result['actual'] = 0

    result['first_max_1_position'] = result['last_max_1_position'] - result['max_num'] + 1
    return result


def all_1_in_sequence(sequence: object):
    all_1_sequences = list()
    repeated_1 = 0

    for i in range(len(sequence)):
        if sequence[i] == 1:
            repeated_1 += 1
        elif repeated_1 > 1:
            all_1_sequences.append([i - 1, repeated_1])
            repeated_1 = 0

    return all_1_sequences

def finished(COLUMNS, LINES, result):
    return False


def viewing_block_position_based_on_available_space(COLUMNS, LINES, result):
    for column in range(COLUMNS):
        values = table[f'c{column}'].split(' ')
        sum = 0

        line_init = None
        line_finish = None

        for i in range(LINES):
            if result[i][column] == 0:
                line_finish = i

                if line_init == None:
                    line_init = i

        if line_init == None and line_finish == None:
            continue

        order = 0
        order_continues = False

        for i in range(LINES):
            actual = result[i][column]

            if actual == -1:
                order_continues = False

            elif actual == 1:
                if not order_continues:
                    values.pop(order)
                    order += 1
                    order_continues = True

            else:
                break

        order = len(values) - 1
        order_continues = False

        for i in range(LINES, 0):
            actual = result[i][column]

            if actual == -1:
                order_continues = False

            elif actual == 1:
                if not order_continues:
                    values.pop(order)
                    order -= 1
                    order_continues = True

            else:
                break

        for num in values:
            sum += int(num)

        margin = (line_finish - line_init + 1) - (sum + len(values) - 1)

        for i in range(len(values)):
            val_num = int(values[i])

            if margin < val_num:
                sum_up = line_init

                for j in range(i):
                    sum_up += int(values[j]) + 1

                for j in range(val_num - margin):
                    result[(sum_up + margin + j), column] = 1

    for line in range(LINES):
        values = table[f'l{line}'].split(' ')
        sum = 0

        column_init = None
        column_finish = None

        for i in range(COLUMNS):
            if result[line][i] == 0:
                column_finish = i

                if column_init == None:
                    column_init = i

        if column_init == None and column_finish == None:
            continue

        order = 0
        order_continues = False

        for i in range(COLUMNS):
            actual = result[line][i]

            if actual == -1:
                order_continues = False

            elif actual == 1:
                if not order_continues:
                    values.pop(order)
                    order += 1
                    order_continues = True

            else:
                break

        order = len(values) - 1
        order_continues = False

        for i in range(COLUMNS, 0):
            actual = result[line][i]

            if actual == -1:
                order_continues = False

            elif actual == 1:
                if not order_continues:
                    values.pop(order)
                    order -= 1
                    order_continues = True

            else:
                break

        for num in values:
            sum += int(num)

        margin = (column_finish - column_init + 1) - (sum + len(values) - 1)

        for i in range(len(values)):
            val_num = int(values[i])

            if margin < val_num:
                sum_left = column_init

                for j in range(i):
                    sum_left += int(values[j]) + 1

                for j in range(val_num - margin):
                    result[line, (sum_left + margin + j)] = 1

    return result


def joining_the_max_sequence_to_others(COLUMNS, LINES, result):
    for column in range(COLUMNS):
        result_bigger = bigger(table[f'c{column}'])

        if result_bigger['First']:
            sequence = list()

            for i in range(LINES):
                sequence.append(result[i][column])

            data_sequence_of_1 = see_1_in_sequence(sequence)

            if data_sequence_of_1['max_num'] > result_bigger['num_second_bigger']:
                for i in range(data_sequence_of_1['first_1_position'], data_sequence_of_1['last_max_1_position']):
                    result[i][column] = 1

        if result_bigger['Last']:
            sequence = list()

            for i in range(LINES):
                sequence.append(result[i][column])

            data_sequence_of_1 = see_1_in_sequence(sequence)

            if data_sequence_of_1['max_num'] > result_bigger['num_second_bigger']:
                for i in range(data_sequence_of_1['last_max_1_position'] + 1, data_sequence_of_1['last_1_position']):
                    result[i][column] = 1

    for line in range(LINES):
        result_bigger = bigger(table[f'l{line}'])

        if result_bigger['First']:
            sequence = list()

            for i in range(COLUMNS):
                sequence.append(result[line][i])

            data_sequence_of_1 = see_1_in_sequence(sequence)

            if data_sequence_of_1['max_num'] > result_bigger['num_second_bigger']:
                for i in range(data_sequence_of_1['first_1_position'], data_sequence_of_1['last_max_1_position']):
                    result[line][i] = 1

        if result_bigger['Last']:
            sequence = list()

            for i in range(COLUMNS):
                sequence.append(result[line][i])

            data_sequence_of_1 = see_1_in_sequence(sequence)

            if data_sequence_of_1['max_num'] > result_bigger['num_second_bigger']:
                for i in range(data_sequence_of_1['last_max_1_position'] + 1, data_sequence_of_1['last_1_position']):
                    result[line][i] = 1

    return result


def cutting_blocks(COLUMNS, LINES, result):
    # Cutting when the size don't fill what is missing

    for column in range(COLUMNS):
            result_bigger = bigger(table[f'c{column}'])
            sequence = list()

            for i in range(LINES):
                sequence.append(result[i][column])

            data_sequence_of_1 = see_1_in_sequence(sequence)

            if result_bigger['num_second_bigger'] == 0:
                lack = LINES - result_bigger['num_bigger']

                if data_sequence_of_1['first_max_1_position'] > lack:
                    for i in range(data_sequence_of_1['first_max_1_position'] - lack - 1):
                        result[i][column] = -1

                if LINES - data_sequence_of_1['last_max_1_position'] > lack and data_sequence_of_1['max_num'] > 0:
                    for i in range(data_sequence_of_1['last_max_1_position'] + lack - 1, LINES):
                        result[i][column] = -1

    for line in range(LINES):
            result_bigger = bigger(table[f'l{line}'])
            sequence = list()

            for i in range(COLUMNS):
                sequence.append(result[line][i])

            data_sequence_of_1 = see_1_in_sequence(sequence)

            if result_bigger['num_second_bigger'] == 0:
                lack = COLUMNS - result_bigger['num_bigger']

                if data_sequence_of_1['first_max_1_position'] > lack:
                    for i in range(data_sequence_of_1['first_max_1_position'] - lack - 1):
                        result[i][column] = -1

                if LINES - data_sequence_of_1['last_max_1_position'] - 1 > lack:
                    for i in range(data_sequence_of_1['last_max_1_position'] + lack + 1, LINES):
                        result[i][column] = -1

    # Cutting when a sequence finished

    for line in range(LINES):
        result_bigger = bigger(table[f'l{line}'])
        sequence = list()

        for i in range(COLUMNS):
            sequence.append(result[line][i])

        data_sequence_of_1 = see_1_in_sequence(sequence)

        all_1_sequences = all_1_in_sequence(sequence)

        actual_line_list = table[f'l{line}'].split(' ')
        int_actual_line_list = [int(value) for value in actual_line_list]
        
        for i in range(len(all_1_sequences)):
            internal_sequence = all_1_sequences[i]
    
            if internal_sequence[1] == result_bigger['num_bigger']:
                try:
                    result[line][internal_sequence[0] - internal_sequence[1]] = -1
                    result[line][internal_sequence[0] + 1] = -1
                except:
                    pass

            elif len(actual_line_list) == len(all_1_sequences):

                for number in int_actual_line_list:
                    if number == internal_sequence[1]:
                        last_sequence = None
                        next_sequence = None

                        if i > 0:
                            last_sequence = all_1_sequences[i - 1]
                        
                        if i < len(all_1_sequences) - 1:
                            next_sequence = all_1_sequences[i + 1]

                        if last_sequence != None:
                            if internal_sequence[0] - last_sequence[0] + last_sequence[1] > result_bigger['num_bigger']:
                                result[line][internal_sequence[0] - internal_sequence[1]] = -1

                                if next_sequence == None:
                                    for i in range(internal_sequence[0] + 1, LINES):
                                        result[line][i] = -1

                        if next_sequence != None:
                            if internal_sequence[1] + next_sequence[0] - internal_sequence[0] > result_bigger['num_bigger']:
                                result[line][internal_sequence[0] + 1] = -1

                                if last_sequence == None:
                                    for i in range(internal_sequence[0] - internal_sequence[1]+ 1):
                                        result[line][i] = -1

    for column in range(COLUMNS):
        result_bigger = bigger(table[f'c{column}'])
        sequence = list()

        for i in range(LINES):
            sequence.append(result[i][column])

        data_sequence_of_1 = see_1_in_sequence(sequence)

        all_1_sequences = all_1_in_sequence(sequence)

        actual_line_list = table[f'c{column}'].split(' ')
        int_actual_line_list = [int(value) for value in actual_line_list]
        
        for i in range(len(all_1_sequences)):
            internal_sequence = all_1_sequences[i]
    
            if internal_sequence[1] == result_bigger['num_bigger']:
                try:
                    result[line][internal_sequence[0] - internal_sequence[1]] = -1
                    result[line][internal_sequence[0] + 1] = -1
                except:
                    pass

            elif len(actual_line_list) == len(all_1_sequences):

                for number in int_actual_line_list:
                    if number == internal_sequence[1]:
                        last_sequence = None
                        next_sequence = None

                        if i > 0:
                            last_sequence = all_1_sequences[i - 1]
                        
                        if i < len(all_1_sequences) - 1:
                            next_sequence = all_1_sequences[i + 1]

                        if last_sequence != None:
                            if internal_sequence[0] - last_sequence[0] + last_sequence[1] > result_bigger['num_bigger']:
                                result[internal_sequence[0] - internal_sequence[1]][column] = -1

                                if next_sequence == None:
                                    for i in range(internal_sequence[0] + 1, LINES):
                                        result[i][column] = -1

                        if next_sequence != None:
                            if internal_sequence[1] + next_sequence[0] - internal_sequence[0] > result_bigger['num_bigger']:
                                result[internal_sequence[0] + 1][column] = -1

                                if last_sequence == None:
                                    for i in range(internal_sequence[0] - internal_sequence[1]+ 1):
                                        result[i][column] = -1

    return result


def main(COLUMNS: int, LINES: int):
    result = np.zeros((LINES, COLUMNS))
    count = 0

    while True:
        past_result = result.copy()
        result = viewing_block_position_based_on_available_space(COLUMNS, LINES, result)
        result = joining_the_max_sequence_to_others(COLUMNS, LINES, result)
        result = cutting_blocks(COLUMNS, LINES, result)

        if finished(COLUMNS, LINES, result):
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