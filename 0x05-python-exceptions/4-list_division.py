#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divlist = []
    i = 0
    res = 0
    while (i < list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            res = 0
        except (ValueError, TypeError):
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        finally:
            divlist.append(res)
        i += 1
    return (divlist)
