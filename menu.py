def menu() -> int:
    print('\n'
          'Информационная система компании ООО "InterSensor"\n'
          '--------------------------------------\n'
          '1 - Вывод сведений, а также их изменение по одному сотруднику\n'
          '2 - Вывод сведений по всем сотрудникам\n'
          '3 - Ввод и запись сведений о новом сотруднике\n'
          '4 - Ввод и запись дополнительных данных\n'
          '0 - Выход из программы\n')

    operation_number = has_operation_number(
        'Введите номер операции: ', [1, 2, 3, 4, 0])
    return operation_number


def has_operation_number(str_1, list_user):
    while True:
        try:
            num = int(input(str_1))
            if num in list_user:
                return num
            else:
                print('Неверный ввод! Повторите, пожалуйста')
        except ValueError:
            print('Неверный символ! Введите число')
