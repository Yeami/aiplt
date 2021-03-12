import numpy as np

if __name__ == '__main__':
    rows = int(input('Input the amount of rows (M): '))
    cols = int(input('Input the amount of cols (N): '))

    matrix = np.empty([rows, cols])
    matrix.fill(0.5)
    np.fill_diagonal(matrix, -1)

    print(f'Matrix ({rows}x{cols}): \n{matrix}')
