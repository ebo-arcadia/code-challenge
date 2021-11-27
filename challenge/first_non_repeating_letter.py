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
# iterate the string
#   ignore case sensitive
# count numbers of each number
# if count of the 1st number
#   return the number
# if occurrence of each letters is more than 1
#   return empty string

def first_non_repeating_letter(str):
    for i in range(len(str)):
        if len(str) == 0:
            break
        letter = str[0]
        if letter == ' ' or letter == '\t':
            continue
        # using count method
        print(letter + ' (using count method) - ', str.count(letter))
        if str.count(letter) > 1:
            return None
        if str.count(letter) == 1:
            return letter
        # using counter
        counter = 1
        for j in range(1, len(str)):
            if letter == str[j]:
                counter += 1
        str = str.replace(letter, '').strip()
        print(letter + ' - ', counter)


# def clean_first_non_repeating_letter(string):
#     first_letter = [x for x in str if string.count(x) == 1]
#     return first_letter


if __name__ == "__main__":
    string_1 = "Mississippi"
    first_non_repeating_letter(string_1)
    string_2 = "apple"
    first_non_repeating_letter(string_2)
    string_3 = "ppyytthhoonn"
    first_non_repeating_letter(string_3)
    # clean_first_non_repeating_letter(string_1)
