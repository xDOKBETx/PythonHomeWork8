from os import system
from menu import menu
from create_base import get_add_employee, read_file, write_file, get_add_field
from show_staff import get_out_all, has_show_or_change


def clear(): return system('cls')


def data_comm():
    escape = True
    data_flag = False
    data = read_file("staff.json")
    if not data:
        data_flag = True
    while escape:
        if data_flag:
            what = 3
            data_flag = False
        else:
            what = menu()
        if what == 1:
            clear()
            has_show_or_change(data)
            write_file(data)
            clear()
        elif what == 2:
            clear()
            get_out_all(data)
            clear()
        elif what == 3:
            clear()
            get_add_employee(data)
            write_file(data)
            clear()
        elif what == 4:
            clear()
            get_add_field(data)
            write_file(data)
            clear()
        else:
            escape = False


data_comm()
