lista = {}
 
def uusi_lentoasema(lentoasema_lista):
    lentoasema = input("Anna lentoaseman nimi: ")
    koodi = input("Anna antaman lentoaseman ICAO-koodi: ")

    print(f"lentoasema {lentoasema}, {koodi} on lisätty.")

    lentoasema_lista[koodi] = lentoasema

    return lentoasema_lista

def lentoasema_haku(lentoasema_lista):

    while True:
        koodi = input("Anna ICAO-koodi. Kun oleet valmis, syötä tyhjämerkki: ")

        if koodi in lentoasema_lista:
            print(f"{koodi} = {lentoasema_lista[koodi]}")

        elif koodi == "":
            break

        else:
            print(f"Koodi {koodi} ei näy listassa")

    return 


while True:
    print("**Valitse seuraavasta luentelosta**")
    print("-1. uusi lentoasema-")
    print("-2. haku-")
    print("-3. quit-")

    pyynto = input()

    if pyynto == "1" or pyynto == "uusi lentoasema":
        lista = uusi_lentoasema(lista)

    elif pyynto == "2" or pyynto == "haku":
        lentoasema_haku(lista)

    elif pyynto == "3" or pyynto == "quit":
        break

    else:
        print("ERROR!")