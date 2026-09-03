import random

summa = 0

noppa = int(input("Monta noppaa halutat heittää: "))

#for loop jatkaa kaikki nopat ovat heitetty
for x in range(noppa):
    
    #heittää noppa
    sivunop = random.randint(1, 6)

    #Lisää nopan luvun kokonaiseen summan
    summa += sivunop

print("Noppien kokonainen summa on " + summa)