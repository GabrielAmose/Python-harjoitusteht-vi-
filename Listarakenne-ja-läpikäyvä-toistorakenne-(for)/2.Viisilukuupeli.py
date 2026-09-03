lista = []

while True:

    luku = input("Anna luku. kun olet valmis, syötä tyhjämerkkijono: ")

    #Jos käyttäjä syöttää tyhjämerkkijono, listasta järjestetään kaikki luvut isosta pieneen
    if luku == "":
        lista.sort(reverse=True, key=int)
        break

    #lisää luku listaan
    lista.append(luku)

#tulostaa 5 isoimista luvuista
for x in range(5):
   
   print(lista[x])
