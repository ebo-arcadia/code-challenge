a_list = ['there', 'bunch', 'of', 'elements', 'with', 'different', 'amount', 'of', 'lengtheeeeeeeeeeee']

min_len = 1

for element in a_list:
    if len(element) < min_len:
        print(f'Caught an element shorter than {min_len} letters')
        break
else:
    print(f'All elements are at least {min_len} letters long')
