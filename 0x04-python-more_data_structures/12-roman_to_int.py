#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    to_reduce = 0
    arabic_num = 0
    i = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return (None)
    strlen = len(roman_string)
    while (i < strlen):
        if (roman_string[i] == "I"):
            to_reduce += 2
            arabic_num += 1
        elif (i > 0 and roman_string[i-1] == "I"):
            arabic_num += rom_num[roman_string[i]] - to_reduce
            print("num: ", to_reduce)
            to_reduce = 0
        else:
            arabic_num += rom_num[roman_string[i]]
        i += 1
    return (arabic_num)
