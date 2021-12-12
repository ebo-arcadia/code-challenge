# example
# given a num, if the number is less than 0, return -1, if num is 0, return 0, if num is greater than 0, return 1

# imperative
def against_zero_imperative(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1

# declarative
def against_zero_declarative(n):
    return (0 if n == 0 else (-1 if n < 0 else 1))

# another example
# given a list of numbers, if a num is less than 0, replace it with 0. If a num is equal or greater than 0, return the number

# imperative
def replace_zero_imperative(list_of_nums):
    new_list = []
    for n in list_of_nums:
        if n < 0:
            new_list.append(0)
        else:
            new_list.append(n)
    return new_list

# declarative
def replace_zero_declarative(list_of_nums):
    return [0 if n < 0 else n for n in list_of_nums]


if __name__ == "__main__":
    print("imperative expected to return 0: ", against_zero_imperative(0))
    print("imperative expected to return -1: ", against_zero_imperative(-100))
    print("imperative expected to return 1: ", against_zero_imperative(99))
    print("-------------------")
    print("declarative expected to return 0: ", against_zero_declarative(0))
    print("declarative expected to return -1: ", against_zero_declarative(-100))
    print("declarative expected to return 1: ", against_zero_declarative(99))
    print("-------------------")
    list_of_nums = [-1, 5, 0, 1, -9, 0, 31]
    print("replace_zero_imperative: ", replace_zero_imperative(list_of_nums))
    print("replace_zero_declarative: ", replace_zero_declarative(list_of_nums))