import random

if __name__ == '__main__':
    list_length = int(input('Input the length of the list: '))
    value_from = int(input('Input the FROM value of the interval: '))
    value_to = int(input('Input the TO value of the interval: '))

    random_list = random.sample(range(value_from, value_to), list_length)
    print('Random list: ', random_list)
