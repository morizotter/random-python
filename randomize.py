import random

l = list(range(1, 17))
print("List: {}".format(l))

random.shuffle(l)
print("Result: {}".format(l))

csv = ','.join(str(e) for e in l)

with open("./random.csv", mode='w') as f:
    f.write(csv)
