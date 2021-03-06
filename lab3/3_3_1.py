def get_list_from_string(string):
    return string.split()


def remove_duplicates(string_list):
    return list(dict.fromkeys(string_list))


if __name__ == '__main__':
    string = input('Input the string: ')
    string_list = get_list_from_string(string)
    string_list_without_duplicates = remove_duplicates(string_list)

    print('\nThe list of all words:')
    for word in string_list_without_duplicates:
        print(word)
