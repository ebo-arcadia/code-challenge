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


def rgb_to_hex_convertor(num1, num2, num3):
    hex_color_code = ""
    if num1 < 0 or num2 < 0 or num3 < 0:
        return "pass"
        # todo: round these nums to the closest valid value
    else:
        hex_num = int(num1) / 16
        integer_part = int(hex_num // 1)
        decimal_part = int((hex_num % 1) * 16)
        print("integer part: ", integer_part)
        print("decimal part: ", decimal_part)

        # todo: find built-in function to convert base-10 int to base-16 int
        for i in range(0, len(DECIMAL)):
            for j in range(0, len(HEXADECIMAL)):
                if DECIMAL[i] == HEXADECIMAL[j]:
                    print(DECIMAL[j])
                    return DECIMAL[j]
                elif integer_part == 10:
                    return "A"
                elif integer_part == 11:
                    return "B"
                elif integer_part == 12:
                    return "C"
                elif integer_part == 13:
                    return "D"
                elif integer_part == 14:
                    return "E"
                elif integer_part == 15:
                    return "F"

        # extra bounds: using int function to convert base-16 to base-10
        base16_to_base10 = int('DC', 16)
        print("converted from base 16 to base 10? ", base16_to_base10)

        hex_color_code += str(integer_part)
        hex_color_code += str(decimal_part)
        print("final hex color code: ", hex_color_code)

        # todo: apply the same code to num2 and num3

        return hex_num


print(rgb_to_hex_convertor(220, 10, 20))
print("values of params out of range: ", rgb_to_hex_convertor(220, -1, 20))
