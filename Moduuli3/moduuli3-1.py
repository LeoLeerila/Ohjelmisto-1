pituus = int(input("Kuhan pituus (cm):\n"))

if pituus < 37:
    print("Kuha on " + str(37 - pituus) + "cm liian lyhyt, se pitää vapauttaa")
else:
    print("Kuha on tarpeeksi pitkä sen voi pitää")