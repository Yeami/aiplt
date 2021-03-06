COORDINATES = {'x': 0, 'y': 0}


def update_x(path):
    COORDINATES['x'] += int(path[1])


def update_y(path):
    COORDINATES['y'] += int(path[1])


def print_coordinates():
    print(f'{COORDINATES["x"]} {COORDINATES["y"]}')


if __name__ == '__main__':
    while True:
        path = input('Input the path: ').split()

        if path[0] == 'North' or path[0] == 'South':
            update_y(path)
        elif path[0] == 'East' or path[0] == 'West':
            update_x(path)
        elif path[0] == 'Treasure!':
            print_coordinates()
            break
        else:
            print('Sorry, unrecognized data format')
