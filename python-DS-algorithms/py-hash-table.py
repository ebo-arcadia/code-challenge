# what is hash?
# what is hashing?
# what is hashing function?
# how does a hash value is generated?
# why using hash value?
# what is a hash table?
# what is collision?
# how does collision get resolved?
# what operations are supported by hash table?
# what are the pros and cons with using hash table?
# what is a hash table data type example in python?
# what are some real world applications for using hash table?
# does hash function have to be a same?

# what is a hash? a value with fixed length generated by mathematical formula
# what is a hash function?
# what is hashing? using mathematical algorithm to convert a key to a hash in data indexing.

# declare a hash / dictionary
my_dict = {'toy': 'marble', 'date': 'holiday', 'location': 'Maryland', 'people': 'lake family'}

# access the dictionary using key
toy = my_dict['toy']
date = my_dict['date']
people = my_dict['people']
print('some key values: ', toy, date, people)

print('-----------------------')

# updating a dictionary
my_dict['toy'] = 'lego'
my_dict['date'] = 'Shanna birthday'
my_dict['location'] = 'home'
my_dict['people'] = 'Sega, Corinne, Liz, Shanna, Jeylan, Lani'

print('updated my_dict: ', my_dict)

print('-----------------------')

# add and remove elements from a hash table
copy_my_dict = my_dict.copy()
print('copy of my_dict: ', copy_my_dict)
copy_my_dict['year'] = 2021
copy_my_dict['irrelevant'] = 'eat and drink'
print('updated copy of my_dict: ', copy_my_dict)
copy_my_dict.clear()
print('cleared copy of my_dict: ', copy_my_dict)

