# Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the
# API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and
# skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in
# MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#
# Input range : 1 <= n < 4000
#
# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

# Examples
# RomanNumerals.to_roman(1000) # should return 'M'
# RomanNumerals.from_roman('M') # should return 1000

# Help
# Symbol	Value
# I	1
# IV 4
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000

# pseudocode
# 1. extract the main significant number
#     1.1 divide the param num with the length of num
#     1.2 store the result to a variable
#     1.3 append the roman char corresponding to the variable value according to the dict
# 2. repeat the above operation till the param num becomes 0
import math


class RomanNumerals:

    @staticmethod
    def to_roman(num):
        dictionary = \
            {
                1: "I",
                4: "IV",
                5: "V",
                9: "IX",
                10: "X",
                40: "XL",
                50: "L",
                90: "XC",
                100: "C",
                400: "CD",
                500: "D",
                900: "CM",
                1000: "M"
            }

        divisor = 1
        while num >= divisor:
            divisor *= 10

        divisor /= 10
        result = ""

        while num:
            significant_num = int(num / divisor)
            result += str(significant_num)

            num = math.floor(num % divisor)
            divisor /= 10

        return result

        # if num in dictionary.keys():
        #     return dictionary[num]
        # elif 1 < num < 4:
        #     roman_str = ""
        #     roman_char = roman_str.ljust(num + len(roman_str), "I")
        #     return roman_char
        # elif 5 < num < 9:
        #     roman_str = "V"
        #     roman_char = roman_str.ljust((num - 5) + len(roman_str), "I")
        #     return roman_char
        # else:
        #     return "invalid num input"

    def from_roman(roman_num):
        return 0


roman_numerals = RomanNumerals()
# print(roman_numerals.to_roman(1))
# print(roman_numerals.to_roman(4))
# print(roman_numerals.to_roman(5))
# print(roman_numerals.to_roman(1000))
# print(roman_numerals.to_roman(2))
# print(roman_numerals.to_roman(9))
print(roman_numerals.to_roman(110))
