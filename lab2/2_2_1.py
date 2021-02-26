import random


def get_negative_list_with_generator(initial_list):
    return [item for item in initial_list if item < 0]


def get_negative_list_without_generator(initial_list):
    new_list = []
    for item in initial_list:
        if item < 0:
            new_list.append(item)
    return new_list


if __name__ == '__main__':
    n = int(input('Input the length of the list: '))
    a = [random.randint(-10, 10) for i in range(n)]

    print('The initial random generated list: ', a)
    print('Negative list using generator: ', get_negative_list_with_generator(a))
    print('Negative list without generator:', get_negative_list_without_generator(a))
