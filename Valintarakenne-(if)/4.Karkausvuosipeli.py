vuosi = int(input("Anna lukuvuosi: "))

#Vuosi on karkausvuosi, jos vuosi on jaollinen 4 ja/tai 100
if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
    print("Vuosi on karkausvuosi.")

#Jos vuosi ei ole jaollinen 4 ja/tai 100
else:
    print("Vuosi ei ole karkausvuosi.")