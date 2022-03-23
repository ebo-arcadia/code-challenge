# what is lambda function? anonymous function used to complete a small task then no longer needed
# syntax: lambda arguments: expression
# what does list comprehension do?
# syntax: list = [ x (var/ops/func) for x in iterable if condition ]
from timeit import timeit, repeat

class Advanced_Python:

    def use_lambda(self):
        lambdaFun1 = lambda x, y: x ** y
        return lambdaFun1(3, 5)

    def use_list_comprehensions(self):
        words = ['Woodstock', 'Gary', 'Tucker', 'Gopher', 'Spike',
                 'Ed', 'Faline', 'Willy', 'Rex', 'Rhino', 'Roo',
                 'Littlefoot', 'Bagheera', 'Remy', 'Pongo', 'Kaa', 'Rudolph',
                 'Banzai', 'Courage', 'Nemo', 'Nala', 'Alvin', 'Sebastian', 'Iago']
        filtered_words = [word for word in words if len(word) <= 3]
        return filtered_words

    def list_comprehensions_mapping(self):

        def get_inits(names):
            inits_list = [name[0] for name in names.split()]
            return '.'.join(inits_list) + '.'

        def execute_get_inits():
            people = ['George Washington', 'John Adams', 'Thomas Jefferson', 'John Quincy Adams']
            inits = [get_inits(person) for person in people]
            return inits

        rt = execute_get_inits()
        return rt

    def roll_dice_nested_loop(self):
        dice_rolls = []
        for x in range(1, 7):
            for y in range(1, 7):
                roll = (x, y)
                dice_rolls.append(roll)
        return dice_rolls


    def roll_dice_list_comprehensions(self):
        dice_rolls = [(a, b) for a in range(1, 7) for b in range(1, 7)]
        return dice_rolls

    def roll_dice_perf_compare(self):
        roll_dice_nested_loop = """
        dice_rolls = []
        for x in range(1, 7):
            for y in range(1, 7):
                roll = (x, y)
                dice_rolls.append(roll)
        return dice_rolls """

        roll_dice_list_comprehensions = """
        dice_rolls = [(a, b) for a in range(1, 7) for b in range(1, 7)]
        return dice_rolls """

        perf_roll_dice_nested_loop = timeit(roll_dice_nested_loop, number=2000, globals=globals())
        perf_roll_dice_list_comp = timeit(roll_dice_list_comprehensions, number=2000, globals=globals())

        print("performance running times for each method: ")
        print(perf_roll_dice_nested_loop, perf_roll_dice_list_comp, sep="\n")
        print("-" * 70)
        print("performance comparison: ")
        print(f'{perf_roll_dice_nested_loop/perf_roll_dice_list_comp:.2%}')

    def roll_dice_comb_nested_loop(self):
        dice_rolls = []
        for x in range(1, 7):
            for y in range(x, 7):
                roll = (x, y)
                dice_rolls.append(roll)
        return dice_rolls

    def roll_dice_comb_list_compreh(self):
        dice_rolls = [(x, y) for x in range(1, 7) for y in range(x, 7)]
        return dice_rolls


if __name__ == "__main__":
    obj = Advanced_Python()
    print(obj.use_lambda())
    print(obj.use_list_comprehensions())
    print(obj.list_comprehensions_mapping())
    print(obj.roll_dice_nested_loop())
    print(obj.roll_dice_list_comprehensions())
    print(obj.roll_dice_comb_nested_loop())
    print(obj.roll_dice_comb_list_compreh())
    print(obj.roll_dice_perf_compare())


