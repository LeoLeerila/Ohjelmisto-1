sukupuoli = input("Syötä biologinen sukupuoli:\n")
hemoglobiini = int(input("Syötä hemoglobiiniarvon (g/l):\n"))

if sukupuoli[0] == "N" or sukupuoli[0] == "n":
    sukupuoli = 0
elif sukupuoli[0] == "M" or sukupuoli[0] == "m":
    sukupuoli = 1

if sukupuoli == 0:
    if hemoglobiini < 117:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini > 175:
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")
elif sukupuoli == 1:
    if hemoglobiini < 134:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini > 195:
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")
else:
    print("Syötetty biologinensukupuoli ei ollut mies tai nainen")