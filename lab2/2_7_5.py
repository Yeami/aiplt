def find_different(first_list, second_list):
    return list(list(set(first_list) - set(second_list)) + list(set(second_list) - set(first_list)))


def find_similar(first_list, second_list):
    return list(set(first_list).intersection(second_list))


if __name__ == '__main__':
    temp_first_list = [10, 20, 30, 40, 50]
    temp_second_list = [10, 20, 35, 45, 50]

    first_list = input('Input the first list: ').split(' ')
    second_list = input('Input the second list: ').split(' ')

    print('Different items in list: ', find_different(first_list, second_list))
    print('Similar items in list: ', find_similar(first_list, second_list))
