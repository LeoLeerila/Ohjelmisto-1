import random

def noppa():
    return random.randint(1, 6)

i = 0
while i != 6:
    i = noppa()
    print(str(i))