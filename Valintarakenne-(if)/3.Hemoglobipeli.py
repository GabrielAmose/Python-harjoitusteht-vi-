suku = input("Mikä on sukupuolesi (mies/nainen): ")
hemo = int(input("Anna hemoglobiiniarvosi (g/dl): "))

#Jos Hemoglobiarvo on liian alhainen
if suku == "mies" and hemo < 134 or suku == "nainen" and hemo < 117:
        print("Hemoglobiiniarvosi on liian alhainen, joten sinun tulee hakeutua lääkärin vastaanotolle.")

#Jos Hemoglobiarvo on normaali
elif suku == "mies" and 134 <= hemo <= 195 or suku == "nainen" and 117 <= hemo <= 175:
        print("Hemoglobiiniarvosi on normaali.")

#Jos Hemoglobiarvo on liian korkea
elif suku == "mies" and hemo > 195 or suku == "nainen" and hemo > 175:
        print("Hemoglobiiniarvosi on liian korkea, joten sinun tulee hakeutua lääkärin vastaanotolle.")