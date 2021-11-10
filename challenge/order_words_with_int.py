# Sort a given string. Each word in the string will contain a single number. This number is the position the word
# should have in the result. Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0). If the input
# string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# pseudocode
# 1. iterate the given sentence and split
# 2. for each word separated by space, iterate each letter and find the integer
# 3. compare two numbers at a time
#       if number is smaller, move the word the num is in to the left
#       otherwise, move on to the next comparison
#       return the sorted sentence
# 4. if sentence is an empty, return an empty string

# found a better pseudocode
# create a tuple of (int, word) for each word in sentence
# create a two-level nested listed comprehension to iterate each letter in the word
# [...for word in split sentence...] --> for each word in the sentence
#       [...for letter in word...] --> for each letter in a word
#            [...if letter is a number...] --> if a letter is a number
#                add a tuple of (int, word) to a new list
#                return the new list

import re


def check_if_num(word):
    for letter in re.findall(r'\d+', word):
        # for letter in word:
        #     if letter.isdigit(): return int(letter)
        return int(letter)
    return None


def order_words_with_int(sentence):
    if not sentence:
        return ""
    words = sentence.split()
    ordered_words = sorted(words, key=check_if_num)
    joined_ordered_sentence = " ".join(ordered_words)
    print(joined_ordered_sentence)
    return joined_ordered_sentence


def refactor_order_words_with_int(sentence):
    # refactor for efficiency
    if not sentence:
        return ""
    print(' '.join(sorted(sentence.split(), key=check_if_num)))
    return ' '.join(sorted(sentence.split(), key=check_if_num))


order_words_with_int("is2 Thi1s T4est 3a")
order_words_with_int("4of Fo1r pe6ople g3ood th5e the2")
refactor_order_words_with_int("is2 Thi1s T4est 3a")
refactor_order_words_with_int("4of Fo1r pe6ople g3ood th5e the2")
