while True:
    
    tuuma = float(input("Anna tuuma: "))

    #Jos tuuma on negatiivinen luku, whilw loop rikkoo
    if tuuma <= 0:
        print("Tuuma ei voi olla negatiivinen.")
        break

    #Jos on luku psitiivinen tai 0, pulostaa tuuma ja mikä se on centtimetreinä
    else:
        print(f"{tuuma} tuumaa on {tuuma * 2.54} senttimetriä.")
        break