from pprint import pprint
num_one = 3214
num_two = 123125235234124312
num_three = 20000000000000000
# is there a way to make the above numbers more readable?

print_all = [type(num_one), type(num_two), type(num_three)]
pprint(print_all)

number_three_more_readable = 2_000_000_000_000_000_000
number_more_readble = 1_123_124_232_234_463
print("more readable num: ", type(number_more_readble))
print("more readable num: ", type(number_three_more_readable))

statement_eval = eval('num_one + num_two')
print('ops_eval = ', statement_eval)

exec('statment_exec = num_three ** 123')

def incomplete_func():
    pass

def to_complete_later():
    ...


def num_eval(num=...):
    if num is ...:
        print("parameter is required for this function")
    elif num is None:
        print("Non integer input is provided ")
    elif isinstance(num, int):
        print(f"finally {num} is passed!")


num_eval()
num_eval('string')
num_eval(123)


