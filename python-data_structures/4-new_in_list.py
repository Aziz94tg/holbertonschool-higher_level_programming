#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    if idx < 0 or idx >= list_len:
        return my_list[:]
    
    new_list = my_list[:]  # make a shallow copy of the list
    new_list[idx] = element
    return new_list
