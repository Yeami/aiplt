INITIAL_DATA = None


def print_line():
    print('-' * 100)


def get_initial_data():
    return [
        {
            'name': 'KC17',
            'amount': 10,
            'headman': 'Ivanov',
        },
        {
            'name': 'KC18',
            'amount': 5,
            'headman': 'Petrov',
        },
        {
            'name': 'KC19',
            'amount': 15,
            'headman': 'Sidorov',
        },
    ]


def print_actions_list():
    print(
        'Please select the action:\n'
        '1) Print amount of students in selected group\n'
        '2) Print name of the headman in selected group\n'
        '3) Create a tuple of groups where the amount of students is not bigger than selected\n'
        '4) Create a tuple of groups where the amount of students is not less than selected\n'
        '5) Change the amount of students in the selected group\n'
        '6) Change the name of the headman in the selected group\n'
        '7) Add new group to the list\n'
        '8) Remove selected group from the list\n'
        '9) Get list of headmans from selected groups\n'
        '10) Exit from program'
    )


def print_amount_of_students_in_group(name):
    return [group.get('amount') for group in INITIAL_DATA if group['name'] == name][0]


def print_name_of_headman_in_group(name):
    return [group.get('headman') for group in INITIAL_DATA if group['name'] == name][0]


def create_tuple_of_groups_where_amount_is_not_bigger_than(amount):
    return tuple(group for group in INITIAL_DATA if group['amount'] <= amount)


def create_tuple_of_groups_where_amount_is_not_less_than(amount):
    return tuple(group for group in INITIAL_DATA if group['amount'] >= amount)


def change_amount_of_students_in_group(name, amount):
    group = [group for group in INITIAL_DATA if group['name'] == name]
    group[0]['amount'] = amount
    return group


def change_name_of_headman_in_group(name, headman):
    group = [group for group in INITIAL_DATA if group['name'] == name]
    group[0]['headman'] = headman
    return group


def add_new_group_to_list(name, amount, headman):
    INITIAL_DATA.append({
        'name': name,
        'amount': amount,
        'headman': headman,
    })


def remove_group_from_list(name):
    return [group for group in INITIAL_DATA if not (group['name'] == name)]


def get_groups_headman_list(names):
    result = ''

    for name in names:
        for group in INITIAL_DATA:
            if name == group['name']:
                result += f"{group['headman']} "
    return result


if __name__ == '__main__':
    INITIAL_DATA = get_initial_data()

    print_line()
    print('Initial group list: ', INITIAL_DATA)

    print_line()
    print_actions_list()

    while True:
        print_line()
        action = int(input('Input the number of action: '))

        print_line()

        if action == 1:
            group_name = input('Input the group name: ')
            result = print_amount_of_students_in_group(group_name)
            print(f'Amount of students in the {group_name} group is {result}')

        elif action == 2:
            group_name = input('Input the group name: ')
            result = print_name_of_headman_in_group(group_name)
            print(f'The name of the headman in the {group_name} group is {result}')

        elif action == 3:
            students_amount = int(input('Input the amount of students: '))
            result = create_tuple_of_groups_where_amount_is_not_bigger_than(students_amount)
            print(f'The tuple of groups where amount is not bigger than {students_amount}: {result}')

        elif action == 4:
            students_amount = int(input('Input the amount of students: '))
            result = create_tuple_of_groups_where_amount_is_not_less_than(students_amount)
            print(f'The tuple of groups where amount is not less than {students_amount}: {result}')

        elif action == 5:
            group_name = input('Input the group name: ')
            students_amount = int(input('Input the amount of students: '))
            result = change_amount_of_students_in_group(group_name, students_amount)
            print(f'New {group_name} group after amount changing: {result}\n')
            print(f'The full list of group: {INITIAL_DATA}')

        elif action == 6:
            group_name = input('Input the group name: ')
            headman = input('Input the new name of the headman: ')
            result = change_name_of_headman_in_group(group_name, headman)
            print(f'New {group_name} group after headman name changing: {result}\n')
            print(f'The full list of group: {INITIAL_DATA}')

        elif action == 7:
            name = input('Input the new group name: ')
            amount = int(input('Input the amount of students: '))
            headman = input('Input the headman of the group: ')
            add_new_group_to_list(name, amount, headman)
            print(f'The full list of group: {INITIAL_DATA}')

        elif action == 8:
            name = input('Input the group name: ')
            INITIAL_DATA = remove_group_from_list(name)
            print(f'The full list of group: {INITIAL_DATA}')

        elif action == 9:
            names = input('Input the group names splitted by space: ')
            result = get_groups_headman_list(names.split(' '))
            print(f'The list of groups headmans: {result}')

        elif action == 10:
            print('See you later...')
            break
