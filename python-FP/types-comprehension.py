# list comprehension
def list_comprehension(num):
    return [n + 1 for n in range(num) if n % 2 == 0]


# set comprehension
def set_comprehension(num):
    return {n * n for n in range(num) if n % 1 == 0}


# tuple comprehension
def tuple_comprehension(num):
    return tuple(n // 2 for n in range(num) if n % 3 == 0)


# iterator comprehension / generator expression
def iterator_comprehension(new_list):
    generator = (word + str("!") for word in new_list if word != " ")
    modified_list = []
    for word in generator:
        modified_list.append(word)
    return modified_list

# useful notes: generator expression or list comprehension?
# - use list comprehension if one wants to use list methods
# - use generator expression when one only wants to iterate data once
# - generator expression takes less memory


if __name__ == "__main__":
    # testing functions
    list_comp = list_comprehension(10)
    print("add 1 to an even number passed to the function: ", list_comp)
    a_set = set_comprehension(20)
    print("double each number in a set: ", a_set)
    a_tuple = tuple_comprehension(60)
    print("perform floor division in a tuple: ", a_tuple)
    new_list = ["go", "bear", "win"]
    print("add ! to each word in a list of words using iterator comprehension: ", iterator_comprehension(new_list))