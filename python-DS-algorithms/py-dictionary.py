# keys in a dictionary defined by {} must be unique and immutable such as string, integer, and tuples
# values don't have to be unique

# create a dictionary
words_dict = {'fruit': 'a natural produce', 'english': 'a language', 'computer': 'a machine can perform functions'}

# access a dictionary
fruit = words_dict['fruit']
print(fruit)
print('------------------')
# shoes = words_dict['shoes'] <== will throw an error because key fruit does not exist in words_dict

# updating (add, modify, or delete) a dictionary
words_dict['shoes'] = 'a commodity people can wear to protect their feet'
print("updated word_dict with key shoes: ", words_dict)
print('------------------')

# delete
class_dict = {'name': 'Neo', 'grade': 5, 'major': 'biology', 'room': 'room A'}
print("class_dict before deletion: ", class_dict)
del class_dict['room']
print("class_dict after deletion: ", class_dict)
class_dict.clear()
print("empty the entire dictionary: ", class_dict)
print('------------------')

# rules for defining the type of key in dictionary:
# key can only be tuple, string, numbers; list won't work
# example
# invalid_dict = {['weather']: 'nice', 'city': 'Boston'}
# print(invalid_dict) <== will throw an error

valid_dict = {1: "FIFO", 'latency': 'low', ('CPU', 'RAM'): 'M1 2nd gen'}
print(valid_dict)






