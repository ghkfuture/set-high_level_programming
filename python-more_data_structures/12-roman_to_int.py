#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_v = 0
    for char in reversed(roman_string):
        val = rom_d.get(char, 0)
        if val >= prev_v:
            total += val
        else:
            total -= val
        prev_v = val
    return total
