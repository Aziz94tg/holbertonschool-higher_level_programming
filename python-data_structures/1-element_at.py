#!/bin/usr/python3

def element_at(my_list, idx):
    list_len = len(my_list)
    if idx < 0 or idx >= list_len:
        return None
    print("{}".format(my_list[idx]))
