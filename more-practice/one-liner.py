# one line if else statement

def one_line_if_else(num_list):
    print(['^_^' if num % 2 == 0 else '>_<' for num in num_list])


def one_line_nested_loop():
    print([(num1, num2) for num1 in range(1, 5) for num2 in range(10, 15)])


def assign_multi_values():
    x, y, *z = ["apple", "coffee", "cellphone", "books", "radio", "internet"]
    print("x: {}, y: {}, z: {}".format(x, y, z))


def find_odd_using_lambda(nums):
    print(list(filter(lambda num: num % 2 != 0, nums)))


def find_type_int(my_list):
    print([item if type(item) is int else None for item in my_list])


# type casting whole list
def str_list_to_int_list(str_list):
    int_list = list(map(int, str_list))
    print(int_list)


def int_list_to_str_list(int_list):
    str_list = list(map(str, int_list))
    print(str_list)


def to_float_list(input_list):
    float_list = [float(item) for item in input_list]
    print(float_list)


if __name__ == "__main__":
    one_line_if_else([2, 3, 10, 11, 12, 20, 31, 90, 33])
    one_line_nested_loop()
    assign_multi_values()
    find_odd_using_lambda([33, 23, 34, 44, 93, 92, 100])
    find_type_int([1, "candle", 10, "lamp"])
    str_list_to_int_list(['1', '12', '123'])
    int_list_to_str_list([100, 1024, 64])
    to_float_list([256, 40, 4, 5, 7, 8])
