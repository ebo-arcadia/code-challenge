# format operation and placeholder refresher
# 1. empty placeholder replaced with a string/numeric value
import collections

def use_placeholder(name, location):
    return {name, location}

a = use_placeholder("Wesker", "Japan")
print(a)
print("Welcome back, {}".format("John!"))

# 2. using variables or keyword inside a placeholder

print("Today's weather in {city} is {weather}".format(city="San Francisco", weather="sunny"))
print('--------------------------')

# create a list of dictionaries

dict1 = {'religion': 'Mon', 'philosophy': 'Tue'}
dict2 = {'biology': 'Wed', 'physics': 'Thur', 'religion': 'Sun'}
chained_list_dicts = collections.ChainMap(dict1, dict2)
print(chained_list_dicts)
# single_map_dict = chain_dicts.maps
print('what happens with calling maps on the list of dictionaries?: ', chained_list_dicts.maps, '\n')
print('all keys in the list of dictionaries: ', 'keys: {}'.format(list(chained_list_dicts.keys())))
print('all values in the list of dictionaries: ', 'values: {}'.format(list(chained_list_dicts.values())))
print('--------------------------')

# print all items in the list of dictionaries
for key, value in chained_list_dicts.items():
    print("key: {} has value: {}".format(key, value))

print('--------------------------')
# find date for physics
print("physics has value {}".format('physics' in chained_list_dicts))

print('--------------------------')

# map re-ordering
# what happens if the order of dictionaries changed when clubbing them?
# behaviors of maps as stacks
gdp_ranking_north = {1: 'US', 2: 'Canada', 3: 'Mexico'}
gdp_ranking_asia = {1: 'China', 2: 'South Korea', 3: 'Japan'}

gdp_total_1 = collections.ChainMap(gdp_ranking_asia, gdp_ranking_north)
print("asia first: ", gdp_total_1.maps)
gdp_total_2 = collections.ChainMap(gdp_ranking_north, gdp_ranking_asia)
print("north america first: ", gdp_total_2.maps)

print('--------------------------')

# update map
# update (add number four to both dicts above)
gdp_ranking_north[4] = 'Brazil'
gdp_ranking_asia[4] = 'Singapore'
gdp_total_1 = collections.ChainMap(gdp_ranking_asia, gdp_ranking_north)
print("asia first adding the 4th country: ", gdp_total_1.maps)
gdp_total_2 = collections.ChainMap(gdp_ranking_north, gdp_ranking_asia)
print("north america first adding the 4th country: ", gdp_total_2.maps)

print('--------------------------')











