lista = {"kalle", "saara"}

while True:

    nimi = input("Syötä nimi. kun olet valmis, syötä tyhjämerkkki: ")

    if nimi == "":
        break

    elif nimi in lista:
        print("Aiemmin syötetty nimi")

    else:
        print("Uusi nimi")
        lista.add(nimi)

for x in lista:
    print(x)