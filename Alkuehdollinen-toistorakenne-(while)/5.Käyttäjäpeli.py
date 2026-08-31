#yritykset
yritys = int(1)

#Tallennetut tunnus ja salasana
savedtunnus = str("python")
savedsalasana = str("rules")

#While loop jatkaa, kunnes ei ole yli 5 yrityksiä
while yritys <= 5:

    #Pyytää käyttäjän tunnus ja salasana
    tunnus = input("Anna tunnus: ")
    salasana = input("Anna salasana: ")

    #Jos tunnus ja salasana ovat oikein, while loop rikkoo
    if tunnus == savedtunnus and salasana == savedsalasana:
        print("Tervetuloa")
        break

    #Lisää +1 yritykset jos tunnus ja/tai salasana on väärin
    print("pääsy evätty")
    yritys += 1
    

