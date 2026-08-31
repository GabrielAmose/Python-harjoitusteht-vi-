import random

#pisten määrä ja montako pisteet ovat ympyrän sisällä
pistem = 0
ympsis = 0

#pyytää käyttäjältä montako pisteet halutaan laittaa 
pisteet = int(input("Montako pisteet haluat?: "))

#kunnes pistemäärä on vähemmän kuin pyydetty maksimi pissteet
while pistem <= pisteet:
    
    #seuraavan pisteen koordinaatit (neliön sisällä)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    coords = (x**2 + y**2)

    #jos pisteen kordinaati on ympyrän sisällä
    if coords <= 1:
        ympsis += 1

    #lisätään pistemäärä +1
    pistem += 1

#laskee ympyrän sisällä olevien pisteiden prosenttiosuuden
ymppint = float(ympsis / pisteet)

#tulostaa tekstin ja mikä on piin likiarvo
print(f"Piin likiarvo on {4 * ymppint}")