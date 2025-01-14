kanta = int(input("Syötä suorakulmion kanta: "))
korkeus = int(input("Syötä sourakulmion pituus: "))

pintaala = kanta * korkeus
piiri = kanta * 2
piiri += korkeus * 2

print("Pinta-ala: " + str(pintaala))
print ("Piiri: " + str(piiri))