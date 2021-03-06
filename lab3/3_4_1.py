def is_palindrome(string):
    for i in range(0, int(len(string) / 2)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


if __name__ == '__main__':
    string = input('Input the word to check is it a palindrome: ')

    if is_palindrome(string):
        print(f'The word "{string}" is a palindrome')
    else:
        print(f'The word "{string}" is not a palindrome')
