# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# The following are examples of expected output values:
#
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

# pseudocode

# create a global string to store the hex representation
# take the first param(num) in rgb()
# divide it by 16
# keep the integer number and leave the reminder
# convert the integer number to its corresponding hexadecimal num
# append the hexadecimal num to the global string
# take the reminder of the first param and multiple it by 16
# convert the reminder to its corresponding hexadecimal num
# append the hexadecimal num to the global string
# repeat the same operation for the 2nd and then the 3rd params
# return global hex color string
# round values of param nums to the valid range

DECIMAL = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
HEXADECIMAL = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]


def base10_to_base16(color_num):
    hex_decimal_dict = '0123456789ABCDEF'
    integer_part = color_num // 16
    decimal_part = color_num % 16
    print("integer part: ", integer_part)
    print("decimal part: ", decimal_part)
    # check if color num is within valid range
    # if not, around it to be valid
    if integer_part > 15:
        integer_part = 15
        decimal_part = 15
    elif integer_part < 0:
        integer_part = 0
        decimal_part = 0
    return str(hex_decimal_dict[integer_part]) + str(hex_decimal_dict[decimal_part])


def rgb_to_hex_convertor(r, g, b):
    r = base10_to_base16(r)
    g = base10_to_base16(g)
    b = base10_to_base16(b)
    return r + g + b


def rgb2hex(r, g, b):

    def validate_rbg(n):
        if n < 0: return 0
        if n > 255: return 255
        return n

    # check if rgb value is within valid bound
    r = validate_rbg(r)
    g = validate_rbg(g)
    b = validate_rbg(b)

    # convert to hex values
    to_hex = "%02x%02x%02x" % (r, g, b)
    return to_hex.upper()


print("testing rgb2hex: ", rgb2hex(220, 10, 20))
print("testing rgb2hex: ", rgb2hex(220, -1, 20))
print("testing rgb2hex: ", rgb2hex(0, 0, 0))
print(rgb_to_hex_convertor(220, 10, 20))
print("testing convertor with helper function: ", rgb_to_hex_convertor(220, -1, 20))
print("testing convertor with helper function: ", rgb_to_hex_convertor(220, 10, 20))
print("testing convertor with helper function: ", rgb_to_hex_convertor(-10, 300, -1))
print("testing convertor with helper function: ", rgb_to_hex_convertor(0, 0, 0))
