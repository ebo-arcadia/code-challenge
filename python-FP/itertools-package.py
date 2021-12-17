# what is python Itertools?
# what are the benefits of using it?
# a fast, memory-efficient collection of tools for handling/creating iterators
# what are iterators?
# data types that can be used in a for loop

# using itertools
import itertools
import operator

# example tool 1: accumulate()
# problem: given a list of nums, multiple each item, find max, add each num

list_nums = [1, 2, 3, 4, 6, 9]
iter_multiple = itertools.accumulate(list_nums, operator.mul)
iter_sum = itertools.accumulate(list_nums)
iter_max = itertools.accumulate(list_nums, max)

print("testing accumulator(): ")
for i in iter_multiple:
    print(i)
for i in iter_sum:
    print(i)
for i in iter_max:
    print(i)

print("---------------- end")

# example tool 2: combinations()
# given a list of elements, create an iterator with unique combinations of two elements
candies = ['marshmallow', 'snickers', 'chocolate bar', 'wax', 'hard candy', 'gum']
unique_combos = itertools.combinations(candies, 2)
for candy in unique_combos:
    print("unique combos of 2 candies: ", candy)

print("---------------- end")

# example tool 3: count()
for i in itertools.count(5, 5):
    print(i)
    if i > 30:
        break

print("---------------- end")

# example tool 4: filterfalse()
# problem: given a list of numbers, create an iterator only returns numbers that are even in the iterable (the list)
list_of_int = [1, 2, 3, 4, 5, 6, 7, 8]


def nums_generator():
    nums_list = []
    for num in itertools.count(1, 1):
        nums_list.append(num)
        if num > 20:
            break
    return nums_list


even_num_only = itertools.filterfalse(lambda x: x % 2 == 0, nums_generator())
for i in even_num_only:
    print("even nums only: ", i)

print("return a list of nums?: ", nums_generator())
print("---------------- end")

# example tool 5: groupby()
# given a list of books, group them by genre
books = [
    {'title': 'modern men search for meaning', 'author': 'Carl Jung', 'genre': 'psychology'},
    {'title': 'the devils', 'author': 'Dostoevsky', 'genre': 'novel'},
    {'title': 'myth and reality', 'author': 'Mircea', 'genre': 'religion'},
    {'title': 'An Ecological Approach to Visual Perception', 'author': 'Goldberg', 'genre': 'psychology'},
    {'title': 'Zorba the Greek', 'author': 'Nikos', 'genre': 'novel'},
    {'title': 'Words with Power', 'author': 'Northrop', 'genre': 'religion'},
    {'title': 'Genius', 'author': 'Hans', 'genre': 'psychology'},
    {'title': 'Cancer Ward', 'author': 'Aleksandr', 'genre': 'novel'},
    {'title': 'The Crisis of Islam-', 'author': 'Bernard', 'genre': 'religion'},
]


def sort_books_by_genre():
    psychology_books = []
    novels = []
    religion_books = []
    for key, group in itertools.groupby(books, key=lambda k: k['genre']):
        if key == 'psychology':
            psychology_books.append(list(group))
        if key == 'novel':
            novels.append(list(group))
        if key == 'religion':
            religion_books.append(list(group))

    # print('psychology: ', psychology_books)
    # print('novels: ', novels)
    # print('religion: ', religion_books)

    return psychology_books, novels, religion_books


print(sort_books_by_genre())

print("---------------- end")

# example tool 6: permutations
# what is the use of permutations?
# used for analyzing sorting algorithms performance, graph theory, genes study, quantum physics

a_list = [1, 2, 3, 4]
possible_combos = itertools.permutations(a_list, r=None)
for combo in possible_combos:
    print(combo)

print("---------------- end")