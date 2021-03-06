if __name__ == '__main__':
    string = input('Input the string: ')
    symbols = input('Input the symbols separated by space: ')

    result = []
    for symbol in symbols.split():
        result.append(f'{symbol}: {string.count(symbol)}')

    print(f'Result: {result}')
