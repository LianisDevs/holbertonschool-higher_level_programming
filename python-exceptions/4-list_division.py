#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        try:
            result = 0.0
            result = my_list_1[i] / my_list_2[i]
            div_list.append(result)

        except ZeroDivisionError:
            print("division by 0")
            div_list.append(0)

        except TypeError:
            print("wrong type")
            div_list.append(0)

        except IndexError:
            print("out of range")
            div_list.append(0)

    return div_list
