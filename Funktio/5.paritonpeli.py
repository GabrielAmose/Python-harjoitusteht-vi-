lista = [6, 3, 5, 8]

#Lisää parilliset numerot uuteen listaan
def parillinenlista(numerot):
    parilista = []
    for x in range(len(numerot)):
        if numerot[x] % 2 == 0:
            parilista.append(numerot[x])

    return parilista

#Tulostaa vanha lista
print(lista)
#Tulostaa uusi lista
print(parillinenlista(lista))
