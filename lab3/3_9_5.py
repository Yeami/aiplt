def split(word):
    return [char for char in word]


if __name__ == '__main__':
    initial_string = input('Input the initial string: ')
    char_list = split(initial_string)

    len_list = len(char_list)
    print(f'Length is {len_list}')

    max_index = len_list - 1
    print(f'Max index is {max_index}')

    result_string = ''
    removed_string = ''
    for index in range(len_list):
        if index != max_index:
            current_char = char_list[index]
            next_char = char_list[index+1]

            if current_char != next_char:
                result_string += current_char
            else:
                removed_string += next_char
        else:
            result_string += char_list[max_index]

    print('Updated string: ', result_string)
    print('Removed chars string without duplicates: ', ''.join(dict.fromkeys(removed_string)))
