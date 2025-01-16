kokonaisluku = int(input("Syötä kokonaisluku: "))
primecount = 2

for i in range(1, kokonaisluku):
    if kokonaisluku%i == 0:
        primecount -= 1
    if primecount == 0:
        break

if primecount == 0:
    print(f"{kokonaisluku} ei ole alkuluku")
else:
    print(f"{kokonaisluku} on alkuluku")