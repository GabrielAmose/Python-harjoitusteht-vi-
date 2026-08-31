pituus = int(input("Terve kalastaja! Anna teidän kuhan pituus (cm): "))

#Jos kuhan pituus on lyhyempi kuin 37cm
if pituus < 37:
    print("Kuhan pituus on liian pieni, joten se pitää päästää takaisin veteen.")

#Jos kuhan pituus on pidempi kuin 37cm
else:
    print("Kuhan pituus on riittävä, joten se voidaan ottaa mukaan.")