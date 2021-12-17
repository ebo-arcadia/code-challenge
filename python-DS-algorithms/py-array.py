import array as arr

# instantiate an array with integers and a string
int_arr = arr.array('i', [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
str_arr = arr.array('u', 'apple')


def print_int_arr():
    for x in int_arr:
        print(x)


def print_str_arr():
    print(str_arr)


# insert num 999 at the end of the int_arr array
int_arr.insert(len(int_arr), 999)
# remove num 10 from the int_arr array
int_arr.remove(10)
# search an element and return the index of it if the element exists
print("index of num 999 in int_arr is: ", int_arr.index(999))
# update num 999 with 888 using the index num of element 999
int_arr[9] = 888


if __name__ == "__main__":
    print_int_arr()
    print("access the first element in int_arr: ", int_arr[0])  # access the array
    print_str_arr()
    print("access the first letter in str_arr: ", str_arr[0])  # access the array
