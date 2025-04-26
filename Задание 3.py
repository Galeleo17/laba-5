import random
from random import randrange

list = []
for i in range(10):
    num = randrange(0,100, 2)
    list.append(num)

print(sorted(list))