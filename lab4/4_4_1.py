import numpy as np


def convert_string_to_integer_list(string):
    return [int(item) for item in string.split(' ')]


if __name__ == '__main__':
    original_list = convert_string_to_integer_list(
        input('Input the elements of the 1D array separated by space: ')
    )

    matrix = np.asarray(original_list)
    print(f'Matrix from entered list: {matrix}')

    condition = input('''Input the condition (e.g. '> 5' or '< 10'): ''').split(' ')
    condition_char = condition[0]
    condition_value = int(condition[1])

    result = matrix[matrix > condition_value] if condition_char == '>' else matrix[matrix < condition_value]

    print(f'Values {condition_char} than {condition_value}: ', result)
