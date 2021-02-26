import math


def print_line():
    print('-' * 50)


def print_type_error():
    print_line()
    print('[Error] The entered value`s type is not a float')


def print_functions(x):
    print_line()
    print(f'Upper func: ln(sin {x} + 0.5), when x < 1')
    print(f'Lower func: (ctg {x}^2) / sqrt(1 - arcsin {x}), when x > 10')


def print_upper_func_error():
    print_line()
    print('[Error] The value of the X is out of the scope for the upper func')


def print_lower_func_error():
    print_line()
    print('[Error] The value of the X is out of the scope for the lower func')


def print_both_func_error():
    print_line()
    print('[Error] The value of the X is out of the scope for both functions')


def upper_func(x):
    print_line()
    print('Start calculating the upper func...')

    try:
        step_1 = math.sin(x)
        print(f'1. sin {x} = {step_1}')

        step_2 = step_1 + 0.5
        print(f'2. sin {x} + 0.5 = {step_2}')

        step_3 = math.log(step_2)
        print(f'3. ln(sin {x} + 0.5) = {step_3}')

        return step_3
    except Exception as e:
        print(f'[Error] Something went wrong during calculations in the upper func: {e}')


def lower_func(x):
    print_line()
    print('Start calculating the lower func...')

    try:
        step_1 = x ** 2
        print(f'1. {x}^2 = {step_1}')

        step_2 = math.cos(step_1) / math.sin(step_1)
        print(f'2. ctg {x}^2 = {step_2}')

        step_3 = math.asin(x)
        print(f'3. arcsin {x} = {step_3}')

        step_4 = 1 - step_3
        print(f'4. 1 - arcsin {x} = {step_4}')

        step_5 = math.sqrt(step_4)
        print(f'5. sqrt(1 - arcsin {x}) = {step_5}')

        step_6 = step_2 / step_5
        print(f'6. (ctg {x}^2) / sqrt(1 - arcsin {x}) = {step_6}')

        return step_6
    except Exception as e:
        print(f'[Error] Something went wrong during calculations in the lower func: {e}')


if __name__ == '__main__':
    print_line()
    try:
        x = float(input('Input the value of the X: '))

        print_functions(x)

        if 1.0 <= x <= 10.0:
            print_both_func_error()
        else:
            upper_y = upper_func(x) if x < 1.0 else print_upper_func_error()
            lower_y = lower_func(x) if x > 10.0 else print_lower_func_error()
    except Exception as e:
        print_type_error()
