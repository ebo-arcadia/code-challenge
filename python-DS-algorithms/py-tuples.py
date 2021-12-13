# a tuple is similar to a list, but a sequence of immutable objects

# how to create a tuple?
my_tuple = ("rock", "water", "air", "fire", ("dark matter", "black hole"))
num_tuple = (1, 2, 3, 4, 5)
string_tuple = "a", "b", "c", "d", "e"
single_item_tuple = ("the universe",)  # comma is required even there is only one element in a tuple

# how to access in tuples?
print("2nd item in my_tuple: ", my_tuple[1])
print("first 3 nums in num_tuple: ", num_tuple[0:3])
print("first 4 nums in string_tuple: ", string_tuple[0:4])

# how to update tuples?
# not possible because tuples are immutable
# single_item_tuple[0] = "the solar system" <-- won't work
combined_new_tuple = my_tuple + num_tuple
print("a combined two tuple: ", combined_new_tuple)

# how to delete tuple?
# it is not possible to delete elements from a tuple
# but one can delete an entire tuple
copy_of_my_tuple = ("rock", "water", "air", "fire", ("dark matter", "black hole"))
print(copy_of_my_tuple)
# del copy_of_my_tuple[0] <-- won't work
del copy_of_my_tuple
# print(copy_of_my_tuple) <-- ill throw an error because the tuple does longer exist

# what are the best tuples operations?
# tuples responds to + or * much like strings with return value as a new tuple not a string
print("length of my_tuple: ", len(my_tuple))
concat_new_tuple = my_tuple + num_tuple + string_tuple + single_item_tuple
print("concatenate several tuples defined above: ", concat_new_tuple)
print("repeat items in concatenated tuple 3 times: ", concat_new_tuple * 3)
if_item_water_exist = "water" in concat_new_tuple
print("item water in tuple?: ", if_item_water_exist)
for t in combined_new_tuple: print(t)

