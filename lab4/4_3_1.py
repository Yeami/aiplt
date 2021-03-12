import numpy as np


def convert_string_to_integer_list(string):
    return [int(item) for item in string.split(' ')]


if __name__ == '__main__':
    original_list = convert_string_to_integer_list(
        input('Input the elements of the 1D array separated by space: ')
    )

    original_matrix = np.asarray(original_list)
    print(f'Matrix from entered list: {original_matrix}')

    index_list = convert_string_to_integer_list(
        input('Input the indexes of the 1D array that you want to move to the submatrix separated by space: ')
    )
    print(f'Result: {original_matrix[index_list]}')
