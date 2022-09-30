import itertools


# flatten nested list
print("----flatten nested list with itertools---")
nested_list = [['a', 'b'], ['c', 'd'], ['e', 'f'], [['school', ['lunch', 'box']]]]
flattened_list = list(itertools.chain.from_iterable(nested_list))
print(flattened_list)
print("-------")

print("-----reverse-------")
a_list = ["a", "b", "c", "d"]
letter = "sos"
reverse_list = a_list[::-1]
reverse_letter = letter[::-1]
print(reverse_list)
print(reverse_letter)

b_list = [1, 2, 3, 4, 5, 10, 50, 100, 121, 888]
b_list.reverse()
print(b_list)
print("-------")

print("-----combine lists-------")
todo_item = ['clean up', 'writing code', 'exercise']
to_plan = ['go to events', 'go to concert', 'travel']
combined_items = []
for x, y in zip(todo_item, to_plan):
    combined_items.append(x)
    combined_items.append(y)
print(combined_items)
print("-------")

print("-----concat strings-------")
new_string = ""
cool_list = ["science", "medicine", "education", "literature"]
for item in cool_list:
    new_string += item
    new_string += " "
print(new_string)
print("-------")

