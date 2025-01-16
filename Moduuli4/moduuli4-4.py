import random
vastaus = random.randint(1, 10)

while 1:
    arvaus = int(input("Syötä arvaus 1..10 väliltä: "))
    if arvaus > vastaus:
        print("Liian suuri arvaus")
    elif arvaus < vastaus:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break