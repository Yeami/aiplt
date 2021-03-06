def count_occurrences(string, substring):
    return len(string.split(substring)) - 1


if __name__ == '__main__':
    string = input('Input the string: ')
    substring = input('Input the substring: ')
    print(f'There are {count_occurrences(string, substring)} occurrences of the substring "{substring}" in the string "{string}"')
