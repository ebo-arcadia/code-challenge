# a list can contain different types of data such as integer and string or nested list

# how to create a list?
my_list = [2021, "San Francisco", "software", ["security", "network"]]

# how to access values in a list?
item_1_in_my_list = my_list[0]
first_item_in_nested_list_in_my_list = my_list[3][0]
first_3_items_in_my_list = my_list[0:3]

# how to update lists?
list_of_course = ["physics", "philosophy", "chemistry", "neuroscience", "math", "sport"]
list_of_course[0] = "computer science"  # replace physics with computer science

# how to delete elements from a list?
# use del if knowing exactly which element
# sport is not a course so how to delete it?
list_of_course_2 = ["physics", "philosophy", "chemistry", "neuroscience", "math", "sport"]

# best operations on list
l = len([1, 2, 3, "cable", "hotel"])  # length of a list returns an integer
list_a = [11, 22, 33]
list_b = [-9, 0, -11]
cancat_2_lists = list_a + list_b  # cancatenation return a new list combined two lists
list_a_5_times = list_a * 5  # repetition return a new list times list a 5 times
is_a_num_in_list_a = 22 in list_a  # membership returns true
for n in list_a: print(n)  # iteration returns all items in list a

if __name__ == "__main__":
    print("a list: ", my_list)
    print("first item in my_list: ", item_1_in_my_list)
    print("first_item_in_nested_list_in_my_list: ", first_item_in_nested_list_in_my_list)
    print("first_3_items_in_my_list: ", first_3_items_in_my_list)
    print("modified list of course: ", list_of_course)
    print("list_2 before deletion: ", list_of_course_2)
    del list_of_course_2[5]
    print("list_2 after deletion: ", list_of_course_2)
    print("length of a list: ", l)
    print("two list combined: ", cancat_2_lists)
    print("list a repeat 5 times: ", list_a_5_times)
    print("check if 22 in list_a: ", is_a_num_in_list_a)
