import re


def check_string(string):
    if re.match("^[a-zA-Z_][a-zA-Z0-9_]*$", string):
        print(f'String "{string}" is OK')
    else:
        print(f'String "{string}" is NOT OK')


if __name__ == '__main__':
    strings = ['_T_t1', '_&Tt1', '2_d#Wa', '2dfWd', 'WwH34G_']
    for string in strings:
        check_string(string)
