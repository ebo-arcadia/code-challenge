import random
from timeit import timeit

initialStr1 = """
all = str(random.randint(1, 100))
for j in range(1000):
    num = random.randint(1, 100)
    all += ", " + str(num) """

initialStr2 = """
all = [str(random.randint(1, 100)) for j in range(1, 1000)]
all = ', '.join(all) """


perf_append_method = timeit(initialStr1, number=2000, globals=globals())
perf_list_compreh = timeit(initialStr2, number=2000, globals=globals())

print("results returned from timeit: ")
print(perf_append_method, perf_list_compreh, sep="\n")
print('-' * 70)

print("compare performance of += ops to list comprehension: ")
print(f'{perf_append_method/perf_list_compreh:.3%}')

















