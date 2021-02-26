import random


def get_list_without_n_using_generator(initial_list, n):
    return [item for item in initial_list if item != n]


def get_list_without_n_using_cycle(initial_list, n):
    new_list = []
    for item in initial_list:
        if item != n:
            new_list.append(item)
    return new_list


if __name__ == '__main__':
    list_length = int(input('Input the length of the list: '))
    n = int(input('Input the N number: '))
    a = [random.randint(-10, 10) for i in range(list_length)]

    print('The initial random generated list: ', a)
    print('List using generator: ', get_list_without_n_using_generator(a, n))
    print('List using cycle:', get_list_without_n_using_cycle(a, n))
