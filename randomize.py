import random

l = list(range(1, 17))
print("List: {}".format(l))

random.shuffle(l)
print("Result: {}".format(l))