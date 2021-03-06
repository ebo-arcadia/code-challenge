import re
import random
from timeit import timeit, repeat

def get_word():
    words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus', 'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()


def green_glass_door_1():
    word = get_word()
    prev_letter = ''
    for letter in word:
        letter = letter.upper()
        if letter == prev_letter:
            return True
        prev_letter = letter
    return False


def green_glass_door_2():
    word = get_word()
    pattern = re.compile(r'(.)\1')
    return pattern.search(word)


perf_door_1 = repeat(green_glass_door_1, number=2000, repeat=4, globals=globals())
perf_door_2 = repeat(green_glass_door_2, number=2000, repeat=4, globals=globals())

print("results from timeit class: ")
print(perf_door_1, perf_door_2, sep="\n")

print("compare for loop and re.compile: ")
print('{:.2%}'.format(sum(perf_door_1)/sum(perf_door_2)))
