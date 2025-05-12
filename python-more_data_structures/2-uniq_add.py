#!/usr/bin/python3

def uniq_add(my_list=[]):
    seen = []
    total = 0
    for i in my_list:
        if i not in seen:
            seen.append(i)
            total += i
    return total
