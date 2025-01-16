while 1:
    tuuma = int(input("Syötä tuuma:\n"))
    if tuuma < 0:
        break
    print(str(tuuma * 2.54))