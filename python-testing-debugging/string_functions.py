import random
import string
import re

def prepend(s, c):
    return c + s


def append(s, c):
    return s + c


def insert(s, c, position):
    return s[0:position] + c + s[position:]

