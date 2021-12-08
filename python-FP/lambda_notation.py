# lambda functions (not how they are typically used)
plus_one = lambda x: x + 1
plus_two = lambda x: plus_one(plus_one(x))
plus_two(0)  # == plus_one(plus_one(0)) == 2
