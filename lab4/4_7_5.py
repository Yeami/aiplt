import math

import matplotlib.pyplot as plt


def convert_string_to_integer_list(string):
    return [int(item) for item in string.split(' ')]


def get_y(x):
    try:
        if x < 1.0:
            return math.log(math.sin(x) + 0.5)
        elif x > 10.0:
            return math.cos(x ** 2) / math.sin(x ** 2) / math.sqrt(1 - math.asin(x))
    except Exception as e:
        return None


def get_lists(range_list):
    x_list = []
    y_list = []

    for x in range(range_list[0], range_list[1] + 1, 1):
        y = get_y(x)
        if y is not None:
            x_list.append(x)
            y_list.append(y)

    return x_list, y_list


def show_chart(x_list, y_list):
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.plot(x_list, y_list)
    plt.show()


if __name__ == '__main__':
    range_list = convert_string_to_integer_list(
        input('Input the range of X separated by space: ')
    )

    x_list, y_list = get_lists(range_list)
    show_chart(x_list, y_list)
