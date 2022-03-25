from collections import namedtuple, defaultdict, Counter

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
    (a, b)
    for a in range(1, 7)
    for b in range(1, 7)
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

# exercise

yankees_1927 = [{'position': 'P', 'name': 'Walter Beall'}, {'position': 'C', 'name': 'Benny Bengough'},
                {'position': 'C', 'name': 'Pat Collins'}, {'position': 'OF', 'name': 'Earle Combs'},
                {'position': '3B', 'name': 'Joe Dugan'}, {'position': 'OF', 'name': 'Cedric Durst'},
                {'position': '3B', 'name': 'Mike Gazella'}, {'position': '1B', 'name': 'Lou Gehrig'},
                {'position': 'P', 'name': 'Joe Giard'}, {'position': 'C', 'name': 'Johnny Grabowski'},
                {'position': 'P', 'name': 'Waite Hoyt'}, {'position': 'SS', 'name': 'Mark Koenig'},
                {'position': '2B', 'name': 'Tony Lazzeri'}, {'position': 'OF', 'name': 'Bob Meusel'},
                {'position': 'P', 'name': 'Wilcy Moore'}, {'position': '2B', 'name': 'Ray Morehart'},
                {'position': 'OF', 'name': 'Ben Paschal'}, {'position': 'P', 'name': 'Herb Pennock'},
                {'position': 'P', 'name': 'George Pipgras'}, {'position': 'P', 'name': 'Dutch Ruether'},
                {'position': 'OF', 'name': 'Babe Ruth'}, {'position': 'P', 'name': 'Bob Shawkey'},
                {'position': 'P', 'name': 'Urban Shocker'}, {'position': 'P', 'name': 'Myles Thomas'},
                {'position': '3B', 'name': 'Julie Wera'}
                ]

organized_yankees_dict = defaultdict(list)
for yankee in yankees_1927:
    organized_yankees_dict[yankee['position']].append(yankee['name'])

print(organized_yankees_dict)
print('*' * 70)
print(organized_yankees_dict['P'])
print('*' * 70)

# using Counter
dice_rolls = [(a, b, c)
              for a in range(1, 7)
              for b in range(1, 7)
              for c in range(1, 7)
              ]

count_3_dice_rolls = Counter(dice_rolls)
print("Dice roll counter:", count_3_dice_rolls, sep="\n")

# undate counter
# standard update? replace key values with pass-in dictionary
grades = {'English':97, 'Math':93, 'Art':74, 'Music':86}
print("grades before update()", grades)
grades.update({'English': 100, 'Physics': 99, 'Biology': 100})
print("grades after update()", grades)
print('*' * 70)

# update in Counter
# update adds values of a iterable or another counter to its own values
tech_competence_scale = Counter(['AWS', 'AWS', 'AWS', 'Python', 'Python', 'Python', 'Java', 'Python'])
print('scale before: ', tech_competence_scale)
tech_competence_scale.update(['AWS', 'AWS', 'AWS', 'Python', 'Python', 'Python', 'Java', 'Python', 'Angular'])
print('scale after: ', tech_competence_scale)
tech_competence_scale.subtract(['Angular'])
print('scale after removing Angular: ', tech_competence_scale)
most_competent = tech_competence_scale.most_common(1)
print('most competent tech skill: ', most_competent)