# what does mapping function do?
# sequentially pass all values of iterable or iterables to a function
# the returns an iterator with new values
# benefit of using mapping? it will not cause index out of range error

def multiply(x, y):
    return x * y


def execute_without_mapping():
    num1 = range(0, 10)
    num2 = range(10, 0, -1)

    multiples = []
    for i in range(len(num1)):
        multiple = multiply(num1[i], num2[i])
        multiples.append(multiple)

    print("execute without mapping")
    for multiple in multiples:
        print(multiple)

    print("%" * 60)


def execute_with_mapping():
    num1 = range(0, 100)
    num2 = range(10, 0, -1)

    multiples = map(multiply, num1, num2)
    print("execute with mapping")
    for multiple in multiples:
        print(multiple)

    print("@" * 60)


def exeute_with_list_comprehension():
    num1 = range(0, 20)
    num2 = range(50, 0, -1)

    multiples = [multiply(num1[i], num2[i]) for i in range(min(len(num1), len(num2)))]
    print("execute with list comprehension")
    for multiple in multiples:
        print(multiple)
    print("@" * 60)


def execute_map_with_lambda():
    num1 = range(1, 20)
    num2 = range(20, 0, -1)

    multiples = map(lambda n: num1[n] * num2[n], range(1, 10, 2))
    print("execute with lambda")
    for multiple in multiples:
        print(multiple)
    print(')' * 90)


# using filter function
# what does it do and how does it do it?
# sequentially pass all values of a iterable or iterables to a function
# return values for which the function returns true


def is_odd(num):
    return num % 2


def execute_without_filter():
    nums = range(1, 10)

    odd_nums = []
    for num in nums:
        if is_odd(num):
            odd_nums.append(num)
    print("execute without filter")
    for odd_num in odd_nums:
        print(odd_num)
    print('#' * 50)

def execute_with_filer():
    nums = range(1, 40)

    odd_nums = filter(is_odd, nums)
    print("execute with filter")
    for odd_num in odd_nums:
        print(odd_num)
    print('(' * 50)

def execute_with_list_comprehension():
    nums = range(1, 50)

    print("execute with list comprehension")
    odd_nums = [num for num in nums if is_odd(num)]
    for odd_num in odd_nums:
        print(odd_num)
    print(('&' * 80))


def execute_filter_with_lambda():
    print("execute filter with lambda")
    odd_nums = []
    for odd_num in filter(lambda num: num % 2 == 1, range(20)):
        odd_nums.append(odd_num)
        # print(odd_num)
    for odd_num in odd_nums:
        print(odd_num)
    print('^' * 30)
    return odd_nums


if __name__ == "__main__":
    execute_without_mapping()
    execute_with_mapping()
    exeute_with_list_comprehension()
    execute_map_with_lambda()
    execute_without_filter()
    execute_with_filer()
    execute_with_list_comprehension()
    execute_filter_with_lambda()