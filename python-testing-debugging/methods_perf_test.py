import random
import time

start_time = time.perf_counter()

numbers = str(random.randint(1, 100))

for j in range(5000):
    for i in range(1000):
        num = random.randint(1, 100)
        numbers += ',' + str(num)

end_time = time.perf_counter()

td1 = end_time - start_time

start_time = time.perf_counter()
for k in range(5000):
    numbers = [str(random.randint(1, 100)) for i in range(1, 1000)]
    numbers = ', '.join(numbers)

end_time = time.perf_counter()

td2 = end_time - start_time

diff_perf = td1 - td2

print(f"""Time alpha: {td1} Time Delta: {td2}""")
print("performance diff: ", diff_perf)