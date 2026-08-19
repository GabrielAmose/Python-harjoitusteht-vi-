#jatka neljön piiri ja pinta-ala
sivu = input("kirjoita neliön sivun pituus: ")
korkeus = input("kirjoita neliön sivun korkeus: ")

piiri = (float(sivu) * 2) + (float(korkeus) * 2)
pinta_ala = float(sivu) * float(korkeus)

print ("Neljön piiri on: " + str(piiri))
print ("Neljön pinta-ala on: " + str(pinta_ala))