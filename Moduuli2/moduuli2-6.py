import random

kolme = ""
nelja = ""

for x in range(0, 3):
    kolme += str(random.randint(0, 9)) + " "
    nelja += str(random.randint(1, 6)) + " "
nelja += str(random.randint(1, 6))

print("kolminumeroinen koodi: \n" + kolme)
print("nelinumeroinen koodi: \n" + nelja)