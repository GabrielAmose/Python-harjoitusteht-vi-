lista = []

sanat = ["ensimmäinen", "toinen", "kolmas", "neljäs", "viimeinen"]

for x in range(5):
    
    city = input(f"Anna {sanat[x]} kaupunki: ")

    #Lisää kaupungit listaan
    lista.append(city)

#Tulostaa kaupungit yksi kerrallaan 
for y in range(5):

    print(lista[y])