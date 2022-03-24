from collections import namedtuple, defaultdict
# gives a name to an element in a tuple and can reference that element by name

Set = namedtuple('Set', 'shoot, defend, jump, crawl')

command = Set('<--', '-->', '^', '/')

print("command to shoot: ")
print(command.shoot)
print("------")
print("command to depend: ")
print(command.defend)
print("------")
print("command to jump: ")
print(command.jump)
print("------")
print("command to crawl: ")
print(command.crawl)

# creating a dictionary to store numbers of dice rolls
dice_rolls = [
    (a,b)
    for a in range(1,7)
    for b in range(1,7)
]

print(dice_rolls)

roll_counts = {}
for roll in dice_rolls:
    if sum(roll) in roll_counts:
        roll_counts[sum(roll)] += 1
    else:
        roll_counts[sum(roll)] = 1

print(roll_counts)

roll_counts_1 = {}
for roll in dice_rolls:
    try:
        roll_counts_1[sum(roll)] += 1
    except KeyError:
        roll_counts_1[sum(roll)] = 1

print(roll_counts_1)

roll_counts_with_default_dict = defaultdict(int)
for roll in dice_rolls:
    roll_counts_with_default_dict[sum(roll)] += 1

print(roll_counts_with_default_dict)

# creating a dict with lambda function
x = defaultdict(lambda: 6)
x['a'] += 1
x['b'] += 2
print(x)
