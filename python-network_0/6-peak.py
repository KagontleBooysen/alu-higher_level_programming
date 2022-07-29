#!/usr/bin/python3
"""A function that finds a pick in a list of integers"""


def find_peak(list_of_integers):
    """
    find peak
    """
    if list_of_integers:
        list_of_integers.sort()
        return (list_of_integers[-1])
    else:
        return None
