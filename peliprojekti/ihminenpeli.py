import random
#Lista on "feeling lucky" varten
lista = ["Metropolia on paras koulu.", "Karhu on minun lempi eläin.", "Onneksi olkoon! Et voittanut mitään.", "Tykkäätkö kahvista?", "Muista juoda vettä."]

#pyytää käyttäjältä nimi ja ikä
name = input("Kirjoita teidän nimi: ")
ika = int(input("Kirjoita teidän ikä: "))

#Jos ikä on alle 12v. ohjelma ilmoitta alaikäsyydestä ja lopettaa ohjelman  
if ika < 12:
        print("Valitettavasti olet liian nuori, kokeile uudestaan kun olet vanhempi")
        
else:
    print("Tervettuloa " + name)

    while True:
        #Päävalikoima
        print("**Valitse seuraavasta luettelosta**")
        print("-vitsi-")
        print("-raketti-")
        print("-feeling lucky-")
        print("-loppu-")

        pyynto = input()

        #Kertoo vitsin
        if pyynto == "vitsi":
            print("Mikä on Suomen hammaslääkäriliiton suosima lomakohde?")
            print("-Fluorida")

        #Tulostaa rakettijakson
        elif pyynto == "raketti":
            print("rakettijakson käynnistyy")
            print("3... 2... 1... WHOOOOOOSH!!!")

        #Tulostaa eri lauseet satunnaisesti
        elif pyynto == "feeling lucky":
            print(random.choice(lista))
             
        #Sammuttaa ohjelman
        elif pyynto == "loppu":
            print ("Kiitos kun pelasit")
            break

        #Tulee virhe jos käyttäjä antaa muu kun pääohjemassa annettiin
        else:
            print("ERROR!")