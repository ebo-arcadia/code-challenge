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
# take the first param in rgb()
# divide it by 16
# keep the whole number and leave the reminder
# take the reminder of the first param and multiple by 16
# return the corresponding digit of the 6-digit hex code
# repeat the same operation for the 2nd and then the 3rd params
# return global hex color string
# round values of params to the valid range


def rgb_to_hex(num1, num2, num3):
    hex_color_code = ""
    if num1 < 0 or num2 < 0 or num3 < 0:
        return "pass"
        # round these nums to 0
    else:
        hex_num = int(num1) / 16
        return hex_num


print(rgb_to_hex(220, 10, 20))
print("values of params out of range: ", rgb_to_hex(220, -1, 20))