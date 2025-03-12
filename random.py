import random

TIMES = 1000
MAX = 6

a = []
for i in range(TIMES):
    a.append(random.randint(1, MAX))

for i in range(MAX):
    print(f'{i + 1} appeared {round((a.count(i + 1) / TIMES * 100), 2)}% of the time.')