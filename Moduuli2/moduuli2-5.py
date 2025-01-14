leiviska = float(input("Syötä leiviskät: "))
naula = leiviska * 20 + float(input("Syötä naulat: "))
luoti = naula * 32 + float(input("Syötä luodit: "))

massa = luoti * 13.3
print(str(massa))
massa = str(massa * 0.001).split(".")
kilot = massa[0]
grammat = str(float(massa[1]) * 0.01)

print("Massa nykymittojen mukaan: " + kilot + " Kilogrammaa ja " + grammat + " grammaa.")