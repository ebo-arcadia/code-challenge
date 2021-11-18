# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
# items. We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item. It must return the
# display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

# Note: For 4 or more names, the number in "and 2 others" simply increases.

# pseudocode
# iterate the list
# if list is empty, return string
# if 1 element, return element with "likes this." in string format
# if 2 elements, return element 1 and element 2 then "like this." in string format
# if 3 elements, return element 1 + , + element 2 and element 3 then "like this" in string format
# if more than 3 elements, return first 2 elements separated by comma, and then total of rest names + like this.


def list_parser(array):
    result = ''
    if 3 >= len(array) > 1:
        arr = []
        for i in range(0, len(array) - 1):
            arr.append(array[i])
        result = ', '.join(arr)
        result += ' and ' + array[-1] + " like this"
    elif len(array) == 1:
        name = array[0]
        result = name + " likes this"
    elif len(array) >= 4:
        arr = [array[0], array[1]]
        for i in range(0, len(array) - 1):
            count = 0
            count += i
        result = ', '.join(arr)
        result += ' and ' + str(count) + " others like this"
    elif len(array) == 0:
        return "no one likes this"
    return result


print(list_parser([]))
print(list_parser(["Peter"]))
print(list_parser(["Jacob", "Alex"]))
print(list_parser(["Max", "John", "Mark"]))
print(list_parser(["Alex", "Jacob", "Mark", "Max"]))


def cleaner_list_parser(array):
    if len(array) == 0:
        return 'no one likes this'
    elif len(array) == 1:
        return '%s likes this' % array[0]
    elif len(array) == 2:
        return '%s and %s like this' % (array[0], array[1])
    elif len(array) == 3:
        return '%s, %s and %s like this' % (array[0], array[1], array[2])
    else:
        return '%s, %s and %s others like this' % (array[0], array[1], len(array) - 2)


print("testing cleaner_list_parser: ")
print(cleaner_list_parser([]))
print(cleaner_list_parser(["Peter"]))
print(cleaner_list_parser(["Jacob", "Alex"]))
print(cleaner_list_parser(["Max", "John", "Mark"]))
print(cleaner_list_parser(["Alex", "Jacob", "Mark", "Max"]))
