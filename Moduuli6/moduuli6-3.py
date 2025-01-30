litrat = 0

def gallonat(gal):
    return gal * 3.785

while litrat >= 0:
    litrat = gallonat(int(input("Syötä gallonat jotka muutetaan litroiksi:\n")))
    if litrat >= 0:
        print(f"{litrat} litraa")