# pattern matching

x, ___, y, z, (a, b) = [1, 2, 3, "3rd_index", ("tuple_item_1", "tuple_item_2")]
print(x, y, z, a, b)
print("---------------------")

a, (b, c), [x, y], d = ("mango", ("school", "education"), ["alpha", "omega"], "home")
print(a, b, c, d)
print(x, y)
print("---------------------")

# swapping variables
i = 0
j = "word"
print("i value before swap: ", i, "j value before swap: ", j)
i, j = j, i
print("i value after swap: ", i, "j value after swap: ", j)
print("---------------------")

n = 10
print("initial value of n: ", n)
current_n, n = n, n + 100
print("set a new var to store current n value: ", current_n, " n with new value after adding 100: ", n)
print("---------------------")

# iterator loop over a list of index/items pairs

def enumerate_list(my_list):
    item_with_even_index = []
    rest_item = []
    for index, item in enumerate(my_list):
        if index % 2 == 0:
            item_with_even_index.append(my_list[index])
        else:
            rest_item.append(my_list[index])
    return (item_with_even_index, rest_item)


my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print("enumerate a list and returns a tuple of two lists: ", enumerate_list(my_list))
print("---------------------")

# iterator loop over multiple list in parallel

def zip_loop_over_multi_lists(list_a, list_b):
    combined_list = []
    for item_in_a, item_in_b in zip(list_a, list_b):
        combined_list.append(item_in_a)
        combined_list.append(item_in_b)
    return combined_list

list_a = ['a', 'b', 'c', 'd', 'e', 'f']
list_b = ['g', 'h', 'i', 'j', 'k', 'l']
print("loop over multiple lists in parallel and combine them: ", zip_loop_over_multi_lists(list_a, list_b))
print("---------------------")

# iterator loop over a dictionary

def find_a_word_in_a_dictionary(words_dict, search_word):
    word_explained = ""
    for key, value in words_dict.items():
        if search_word in key:
            word_explained += words_dict[key]
    return word_explained

words_dict = {"apple": "a type of fruit", "school": "an institution", "Austin": "a city in Taxes"}
print("find the definition of word apple in words_dict: ", find_a_word_in_a_dictionary(words_dict, "apple"))
print("---------------------")

# advanced pattern matching combining enumerate and zip parallel looping
# loop over two lists of numbers, add them up, store total and index of each sum to a new dictionary
def advanced_looping(list_a, list_b):
    sum_list = {"index": [], "value": []}
    for indx, (a, b) in enumerate(zip(list_a, list_b)):
        sum_a_b = a + b
        print(sum_a_b)
        sum_list["value"] += str(sum_a_b)
        sum_list["index"] += str(indx)
    print("sum list: ", sum_list)
    return sum_list

list_a = [1, 2, 3, 4]
list_b = [15, 16, 17, 20]
print(advanced_looping(list_a, list_b))


