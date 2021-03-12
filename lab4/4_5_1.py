import numpy as np

if __name__ == '__main__':
    variant = 5
    size = int(input('Input the size of the matrix (K): '))

    matrix = np.zeros([size, size], int)
    np.fill_diagonal(matrix, variant)
    matrix = np.fliplr(matrix)

    print(f'Matrix ({size}x{size}): \n{matrix}')
