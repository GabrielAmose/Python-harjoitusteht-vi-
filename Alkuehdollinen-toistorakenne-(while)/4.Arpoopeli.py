import random
#Satunnainen numero 1-10
arpo = random.randint(1, 10)

while (True):
    
    luku = int(input("Anna luku 1-10: "))

    #Jos luku on liian pieni, while loop jatkaa
    if luku < arpo:
        print("Liian pieni arvaus.")

    #Jos luku on liian iso, while loop jatkaa
    elif luku > arpo:
        print("Liian suuri arvaus.")

    #Jos on oikein, while loop rikkoo   
    else:
        print("Arvasit oikein!")
        break