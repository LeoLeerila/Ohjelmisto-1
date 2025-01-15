leiviska = float(input("Syötä leiviskät: \n"))
naula = leiviska * 20 + float(input("Syötä naulat: \n"))
luoti = naula * 32 + float(input("Syötä luodit: \n"))

massa = luoti * 13.3
massa = str(round(massa / 1000, 5)).split(".")
kilot = massa[0]
grammat = str(float(massa[1]) / 100)

print("Massa nykymittojen mukaan: \n" + kilot + " kilogrammaa ja " + grammat + " grammaa.")