def get_out_all(data):
    print('Персональные данные сотрудников\n')
    for worker in data:
        for key, value in worker.items():
            print(f'{key}: {value}')
        print('_________________________')
    input('Для выхода в меню нажмите Enter')


# noinspection PyGlobalUndefined
def has_show_or_change(data):
    global employee
    print('Персональные данные сотрудников\n')
    for employee in data:
        for key, value in employee.items():
            print(f'{key}: {value}')
        what = input('Внести изменения?:\n(ДА - 1, Вернуться в главное меню - 2, Чтобы продолжить просмотр или '
                     'изменение данных следующего сотрудника нажмите Enter )\n')
        if what == '1':
            for key, value in employee.items():
                print(f'{key}: {value}')
                item = input(f'{key}, внести изменения?\n'
                             '(ДА - 1, НЕТ - Enter): ')
                if item == '2':
                    employee[key] = input(f'{key}: ')
                    if key == 'ФИО':
                        employee[key] = employee[key].title()
        elif what == '2':
            return employee
    return employee
