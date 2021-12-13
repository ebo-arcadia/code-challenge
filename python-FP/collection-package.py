# what is python Collection module?
# what does it do?
# what is an container (object stores other objects such as tuples and list and provide ways to access and iterate them)
# how to use Collection?
# what functions does the Collection package provide?

# example
# counter as a subclass of dictionary, keep the count of elements in an iterable

from collections import Counter
from collections import ChainMap

# create Counter with a sequence of items in a list
print(Counter(["apple", "apple", "apple", "banana", "banana", "grapefruit"]))

# create Counter with dictionary
print(Counter({"classrooms": 30, "teacher": 10, "students": 100}))

# create Counter with key argument
print(Counter(Asian=3, White=4, African=5))

# example
# ChainMap encapsulates dictionaries into a single unit and returns a list of dictionaries

dict_car = {'engine': 'vfh31', 'mileage': 3000, 'make': 'toyota'}
dict_book = {'title': 'return to the source', 'author': 'Wilson', 'genre': 'spirituality'}
dict_home = {'size': 'single family', 'bedrooms': 3, 'price': 150000}


list_of_dictionaries = ChainMap(dict_home, dict_book, dict_car)
print(list_of_dictionaries)

# how to access keys and values from ChainMap?
# method 1: using the key name
title = list_of_dictionaries["title"]
print(title)
# method 2: using built-in keys()
keys = list(list_of_dictionaries.keys())
print(keys)
values = tuple(list_of_dictionaries.values())
print(values)

# how to manipulate operations using chain map?
# example: adding a new dict to an existing one?
# a new dict
dict_biology = {'cells': 'transmitter', 'organs': 'liver'}
dict_computer = {'processor': 'intel core i9', 'RAM': 256}
dict_bio_com = ChainMap(dict_biology, dict_biology)
print("chained dictionaries of bio and computer: ", dict_bio_com)
dict_student = {'name': 'Daniel', 'major': 'computer science', 'age': 33}
new_dict = dict_bio_com.new_child(dict_student)
print('new_child used to append dict_student to dict_bio_com: ', new_dict)

# further operatons with collection package
# OrderedDict
# DefaultDict
# NamedTuple
# DeQue
# UserDict
# UserList
# UserString


