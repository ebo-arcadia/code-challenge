# what is a set?
# it is a collection of items not in any particular order
# with several exceptions in python
# no duplicate elements; elements are immutable but the set as a whole is; no index

# how to create a set?
days_list = ["Mon", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Sun"]
days_set = set(days_list)
months = {"Jan", "Feb", "Mar"}
years = {1988, 2000, 2021}
print(days_set)
print(type(months))
print(type(years))
print(type(days_set))
print("------------------------")

# how to access an individual element is a set?
# it can't but one can get a list of individual element with looping

for day in days_set:
    print("single day in days_set: ", day)

print("------------------------")

# how to add item to a set?
days_set.add("Sabbath Day")
days_set.add("Mon")  # won't work because element can not be duplicated in a set
print("new set adding en element: ", days_set)
print("------------------------")

# how to remove an element from a set?
days_set.discard("Tue")
print("new set with Tue removed: ", days_set)
print("------------------------")

# Union of sets
# it operates on multiple sets and return a new set with distinct elements
set_a = {"bank", "school", "post office"}
set_b = {"bank", "gym", "store"}
set_c = {"bank", "store", "theater", "coffee shop"}
all_places = set_a | set_b | set_c
print("new set with union operation: ", all_places)
print("------------------------")

# intersection of sets
# it operates on multiple sets and return a new set with only common elements from all sets
set_a = {"bank", "school", "post office"}
set_b = {"bank", "gym", "store"}
set_c = {"bank", "church", "theater", "coffee shop"}
unique_place = set_a & set_b & set_c
print("common places in all sets with intersection operation: ", unique_place)
print("------------------------")

# difference of sets
# it operates on two sets and returns elements that are only in the first set
set_a = {"bank", "school", "post office"}
set_b = {"bank", "gym", "store", "school"}
only_in_set_a = set_a - set_b
print("elements only in set_a with difference operation: ", only_in_set_a)
print("------------------------")

# compare sets
# it operates on two sets, check if a set is a subset or a superset of another set, returns ture or false
set_a = {"bank", "school", "post office"}
set_b = {"bank", "gym", "store", "school", "post office"}
set_c = {"bank", "gym", "store", "school", "post office", "church", "theater", "coffee shop"}
set_d = {"bank", "school", "post office"}
set_e = {"bank", "school", "post office"}
if_subsets = set_a <= set_b <= set_c
if_supersets = set_c >= set_b
compare_set_d_e = set_d == set_e
print("subsets?: ", if_subsets)
print("supersets?: ", if_supersets)
print("same sets?: ", compare_set_d_e)
print("------------------------")