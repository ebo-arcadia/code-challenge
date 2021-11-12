# Return: a string formatted as a list of names separated by commas except for the last two names, which should be
# separated by an ampersand.
#
# Example:
#
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'
#
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'
#
# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'
#
# namelist([])
# # returns ''

# pseudocode
# create a new empty string
# iterate array to get hashes
#     iterate hashes
#         get the first key value
#             insert the first key value to the new string
#         get the rest key value except the last one
#             insert the rest key values into the new string separated by comma
#         get the last key value
#             insert the last key value with ampersand in front
#     return the new string

def array_hash_formatter(array):
    string = ''
    if len(array) != 0:
        arr = []
        for i in range(0, len(array) - 1):
            arr.append(array[i]['name'])
        string = ', '.join(arr)
        string += ' & ' + array[-1]['name'] if string != '' else array[-1]['name']

    return string


def efficient_formatter(array):
    # if there are more than one name
    # iterate array of hashes
    # join all values of keys except the last one
    # join the last value
    # if there is less or equal one key-value pair in array, return that value
    # else if empty return empty string
    if len(array) > 1:
        return '{} & {}'.format(', '.join(item['name'] for item in array[:-1]), array[-1]['name'])
    elif array:
        return array[0]['name']
    else:
        return ''


array1 = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
array2 = [{'name': 'Bart'}, {'name': 'Lisa'}]
array3 = [{'name': 'Bart'}]
array4 = []
print(array_hash_formatter(array1))
print(array_hash_formatter(array2))
print(array_hash_formatter(array3))
print(array_hash_formatter(array4))

print("efficient formatter output: ")
print(efficient_formatter(array1))
print(efficient_formatter(array2))
print(efficient_formatter(array3))
print(efficient_formatter(array4))
