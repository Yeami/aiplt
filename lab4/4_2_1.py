import numpy as np


if __name__ == '__main__':
    rows = int(input('Input the amount of rows (M): '))
    cols = int(input('Input the amount of cols (N): '))

    matrix = np.empty([rows, cols])
    matrix.fill(0.5)
    np.fill_diagonal(matrix, -1)

    print(f'\nMatrix ({rows}x{cols}):\n{matrix}\n')

    left_top_index = [int(item) for item in input('Input the left top index separated by space: ').split(' ')]
    right_bottom_index = [int(item) for item in input('Input the right bottom index separated by space: ').split(' ')]

    print(f'\nIndexes: [{left_top_index}, {right_bottom_index}]')
    print(f'\nSubmatrix:\n{matrix[np.ix_(left_top_index, right_bottom_index)]}')
