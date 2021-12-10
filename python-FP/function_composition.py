# Functional programming principle: composition not steps

# example
# write a function perform multiple operations on a string
# imperative approach (focus on steps)

def multi_function_operation_imperative(x):
    func_0 = x + 1  # step 1
    func_1 = func_0(func_0)  # step 2
    func_2 = func_1(func_1)  # step 3
    func_3 = func_2(func_2)  # step 4
    return func_3


# declarative approach (function composition)
def multi_function_operation_declaritive(x):
    return func_3(func2(func_1(func_0(x))))


# another example write a function to parse a string, make them lower case, split it into a list of words,
# ascend sort them, and find the index of a particular word
#
# imperative (steps)

def string_parser_imperative(x):
    lowered = x.lower()  # step one, lower the case of each letter in the string
    split_li = lowered.split()  # step two, split the string into a list of words
    sorted_li = sorted(split_li)  # step three, sort the list
    indexed = sorted_li.index("how")  # step four, find the index of a particular item occurs 1st time
    return indexed


# declarative (composition)

def string_parser_declarative(y):
    result = (sorted(y.lower().split()).index("may"))
    return result


if __name__ == "__main__":
    x = "HOW DO BECOME A GOOD ENGINEER"
    print(string_parser_imperative(x))
    y = "TOMORROW MAY RAIN"
    print(string_parser_declarative(y))
