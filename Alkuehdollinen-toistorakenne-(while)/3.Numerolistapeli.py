#Lista jonka lisätään luvut
lukujono = []

while (True): 
     
    luku = input("Anna luku. Kun olet valmis, syötä tyhjä merkkijonoon: ")

    #Jos input on tyhjä, while loop rikkoo
    if luku == "":  
        break   

    #lisää luku lukujonoon
    lukujono.append(luku)

#Järjestää luvut lukujonosta
lukujono.sort()

#Tulostaa teksti ja luvut järjrstyksessä
print("Syöttämäsi luvut järjestyksessä: ", lukujono)
    