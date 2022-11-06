import json
import os


def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf8') as file_reading:
            data = json.load(file_reading)
    else:
        data = []
        print('\n'
              'Информационная система IT-компании ООО "interSensor"\n'
              'Введите данные первого сотрудника\n')
    return data


def write_file(data, file_reserve='staff.json'):
    with open(file_reserve, 'w', encoding='utf8') as file_writing:
        json.dump(data, file_writing, ensure_ascii=False, indent=4)


def get_add_employee(data: list) -> list:
    if not data:
        employee: dict = {'ФИО': input('Введите ФИО: ')}
        employee['ФИО'] = employee['ФИО'].title()
    else:
        sample = data[0]
        employee = {}
        for i in sample:
            employee[i] = input(f'Введите {i}: ')
            if i == 'ФИО':
                employee[i] = employee[i].title()
            else:
                employee[i] = employee[i].capitalize()
    data.append(employee)
    return data


def get_add_field(data):
    signification = input('Введите название нового поля: ')
    for x in data:
        if x != data[0]:
            x[signification] = '*'
        else:
            print(x['ФИО'])
            x[signification] = input('Введите значение: ')
    return data
