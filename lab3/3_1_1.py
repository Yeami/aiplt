def count_digits(string):
    return sum(c.isdigit() for c in string)


if __name__ == '__main__':
    string = input('Input the string: ')
    print(f'There are {count_digits(string)} digits in the string {string}')
