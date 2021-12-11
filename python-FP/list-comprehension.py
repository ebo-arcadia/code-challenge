# simple loops operation such as construct, modify a list or a string can be accomplished via list comprehension

# example
# copy a list of numbers, add 1 to each number

# imperative approach (steps using for loop)

def add_one_to_a_list_imperative(current_list):
    new_list = []
    for item in current_list:
        if current_list:
            new_list.append(item + 1)
        else:
            return "the list is empty"
    return new_list


# declarative approach (using list comprehension)
def add_one_to_a_list_declarative(current_list):
    return [x + 1 for x in current_list]


# testing each function
current_list = [1, 2, 3, 4]
imperative = add_one_to_a_list_imperative(current_list)
print(imperative)
declarative = add_one_to_a_list_declarative(current_list)
print(declarative)


# example
# reverse each word in a string

# imperative approach using for loop
def reverse_word_in_a_str_imperative(current_sentence):
    new_sentence = ""  # using a stack to store modified sentence
    words = current_sentence.split()
    if words:
        for word in words:
            new_sentence += " " + word[::-1]
    else:
        return "the sentence is empty"
    return new_sentence[1:]


# declarative approach using list comprehension
def reverse_word_in_a_str_declarative(current_sentence):
    return " ".join(word[::-1] for word in current_sentence.split())


# testing functions
current_str = "the weather is nice today"
x = reverse_word_in_a_str_imperative(current_str)
print(x)
y = reverse_word_in_a_str_declarative(current_str)
print(y)
