# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that
# is not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in
# the string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should
# return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

# pseudocode

# create a dictionary with key for a character and value as the occurrence
# create a copy of the string ignoring case sensitive
# if char is not in dict, store it in dictionary with value of 1
# if char is in dict, increments value as occurrence in dict
# check if the number of occurrences is one, look for the original one in original string using the same index
# if count of the 1st character is 1
#   return the character

# def first_non_repeating_letter(str):
#     for i in range(len(str)):
#         if len(str) == 0:
#             return ''
#         letter = str[0]
#         if letter == ' ' or letter == '\t':
#             continue
#         # using count method
#         count_nums = str.count(letter)
#         print(letter + ' (using count method) - ', count_nums)
#         if count_nums > 1:
#             return None
#         if count_nums == 1:
#             return letter
#         # using counter
#         counter = 1
#         for j in range(1, len(str)):
#             if letter == str[j]:
#                 counter += 1
#         str = str.replace(letter, '').strip()
#         print(letter + ' - ', counter)


def first_non_repeating_letter(string):
    str_counts = {}
    lower_string = string.lower()
    for char in lower_string:
        if char in str_counts:
            str_counts[char] = str_counts[char] + 1
        else:
            str_counts[char] = 1
    for char in lower_string:
        if char in str_counts and str_counts[char] == 1:
            index = lower_string.find(char)
            return string[index]
    return ''


def clean_non_repeating_letter(str):
    for x in str:
        if str.lower().count(x.lower()) == 1:
            return x
    return ''


if __name__ == "__main__":
    string_1 = "mississippi"
    print(first_non_repeating_letter(string_1))
    print(clean_non_repeating_letter(string_1))
    string_2 = "apple"
    print(first_non_repeating_letter(string_2))
    print(clean_non_repeating_letter(string_2))
    string_3 = "ppyytthhoonn"
    print('should return none or empty string: ', first_non_repeating_letter(string_3))
    print('should return none or empty string: ', clean_non_repeating_letter(string_3))
