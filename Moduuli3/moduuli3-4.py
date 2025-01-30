vuosi = int(input("Syötä vuosi:\n"))

if vuosi%4 == 0 and vuosi >= 400:
    print("Vuosi on karkaus vuosi")
else:
    print("Vuosi ei ole karkaus vuosi")