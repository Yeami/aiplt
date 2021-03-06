if __name__ == '__main__':
    amount = int(input('Input the amount of P letters: '))

    print(amount * ' ___   ')
    print(amount * '|   \  ')

    line = ''
    for item in range(amount):
        line += f'| {item + 1}  | '
    print(line)

    print(amount * '|___/  ')
    print(amount * '|      ')
    print(amount * '|      ')
