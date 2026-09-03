cap = False

luku = int(input("Anna luku ja kerron sinulle jos se on alkuluku: "))

#0 ja 1 eivät ole alkulukuja
if luku == 0 or luku == 1:
    cap = True

else:
    #Tarkistaa jos 2 - annettu luku ovat jaollinen annettulla luvulla
    for x in range(2, luku):
        
        #Jos on jaollinen, luku ei ole alkuluku
        if luku % x == 0:
            cap = True

#Jos luku ei ole alkuluku
if cap == True:
    print(f"{luku} ei ole alkuluku")

#Jos luku on alkuluku 
else:
    print(f"{luku} on alkuluku")