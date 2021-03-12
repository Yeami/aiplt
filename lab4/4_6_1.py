import numpy as np


def fill_matrix(diagonal, variant=5):
    np.fill_diagonal(diagonal, variant)


if __name__ == '__main__':
    matrix = np.zeros([7, 7], int)

    fill_matrix(diagonal=matrix[3:])
    fill_matrix(diagonal=matrix[:, 3:])
    fill_matrix(diagonal=np.fliplr(matrix[3:]))
    fill_matrix(diagonal=np.fliplr(matrix[:, :4]))

    print(f'Matrix ({7}x{7}):\n{matrix}')
