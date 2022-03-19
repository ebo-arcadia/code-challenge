import random
from timeit import repeat

initialStr1 = """
all = str(random.randint(1, 100))
for j in range(1000):
    num = random.randint(1, 100)
    all += ", " + str(num) """

initialStr2 = """
all = [str(random.randint(1, 100)) for j in range(1, 1000)]
all = ', '.join(all) """


perf_append_method = repeat(initialStr1, number=2000, repeat=3, setup="import random")
perf_list_compreh = repeat(initialStr2, number=2000, repeat=3, globals=globals())

print("results returned from timeit: ")
print(perf_append_method, perf_list_compreh, sep="\n")
print('-' * 70)

# print(type(perf_append_method))
# print(type(perf_list_compreh))

print("compare performance of += ops to list comprehension: ")
print(f'{sum(perf_append_method)/sum(perf_list_compreh):.3%}')

















