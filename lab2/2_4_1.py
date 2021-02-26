import random

if __name__ == '__main__':
    _list = [random.randint(-10, 10) for i in range(10)]
    print('Generated list: ', _list)

    value = int(input('Input the number that you want to insert: '))
    index = int(input('Input the index of the list where you want to insert item: '))

    _list[index:index] = [value]
    print('Updated list: ', _list)
