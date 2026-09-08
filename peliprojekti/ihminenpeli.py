import random
rahaa = 0
reppu = []
#Lista on "feeling lucky" varten
lista = ["Metropolia on paras koulu.", "Karhu on minun lempi eläin.", "Onneksi olkoon! Et voittanut mitään.", "Tykkäätkö kahvista?", "Muista juoda vettä."]

#Kruuna vai klaava peli
def kruunavaiklaava():

    #Valitsee kolikon puoli satunnaisesti
    kolikko = ["kruuna", "klaava"]
    puoli = random.choice(kolikko)
    palkinto = 0

    print("Heitetään kolikko!")

    while True: 
        #valitsee puoli
        vast = input("kruuna vai klaava: ")

        #Pelaaja voittaa 10€ jos arvaa oikein 
        if vast == puoli:
            print("Se on " + puoli)     
            print("Sinä voitit!!!")
            print("Voitit 10 Euroo")
            palkinto += 10
            return palkinto

        #Pelaaja häviää jos arvaa väärin
        elif vast == "klaava" != puoli or vast == "kruuna" != puoli:
            print("Se on " + puoli)     
            print("Sinä hävisit...")
            return palkinto

        #Peli aloittaa uudestaan jos vastaus ei ole "kruuna" tai "klaava"
        else:
            print("Syöte oli virheelinen, yritä uudestaan")    

#Kauppa
def kauppa(euro, repp):
    print("Tervettuloa kauppaan!")

    while True:

        print(f"Rahaa: {euro}€")

        #Tuotteiden valikoima
        print("**Tuotteet**")
        print("-mehu- 2€")
        print("-karkkipussi- 3€")
        print("-paita- 10€")
        print("-pokaalii- 20€")
        print("-takaisin-")
        tuote = input("Mitä haluat ostaa: ")

        #Jos käyttäjä kirjoitti tuotteen oikein ja on riittävästi rahaa
        if tuote == "mehu" and euro >= 2:
            euro -= 2
            repp.append("-Mehu")

        elif tuote == "karkkipussi" and euro >= 3:
            euro -= 3
            repp.append("-Karkkipussi")

        elif tuote == "paita" and euro >= 10:
            euro -= 10
            repp.append("-Paita")

        elif tuote == "pokaali" and euro >= 20:
            euro -= 20
            repp.append("-Pokaali")

        #Jos haluaa palaa takaisin päävalikoimaan
        elif tuote == "takaisin":
            return euro, repp

        #Jos käyttäjä kirjoitti väärin tai ei ole riittävästi rahaa
        else:
            print("ERROR!")

#Reppu
def varasto(raha, reppu):
    while True:
        print("**Varastluettelo**")
        print(f"-Rahaa: {raha}")
        print("*tavarat*")

        #tulostaa tavarat yksi kerrallaan
        for x in range(len(reppu)):
            print(reppu[x])

        print("-takaisin-")
        back = input()

        #Jos haluaa palaa takaisin päävalikoimaan
        if back == "takaisin":
            return

        #Jos käyttäjä kirjoitti väärin
        else:
            print("ERROR!")

#PELI ALKAA     
#pyytää käyttäjältä nimi ja ikä
name = input("Kirjoita teidän nimi: ")
ika = int(input("Kirjoita teidän ikä: "))

#Jos ikä on alle 12v. ohjelma ilmoitta alaikäsyydestä ja sammuttaa ohjelman  
if ika < 12:
        print("Valitettavasti olet liian nuori, kokeile uudestaan kun olet vanhempi")
        
else:
    print("Tervettuloa " + name)

    while True:
        #Päävalikoima
        print("**Valitse seuraavasta luettelosta**")
        #Projekti 2
        print("-vitsi-")
        print("-raketti-")
        print("-feeling lucky-")
        #Projekti 3
        print("-peli-")
        print("-kauppa-")
        print("-reppu-")
        print("-loppu-")

        pyynto = input()

        #Kertoo vitsin
        if pyynto == "vitsi":
            print("Mikä on Suomen hammaslääkäriliiton suosima lomakohde?")
            print("-Fluorida")

        #Tulostaa rakettijakson
        elif pyynto == "raketti":
            print("Rakettijakson käynnistyy")
            print("3... 2... 1... WHOOOOOOSH!!!")

        #Tulostaa eri lauseet satunnaisesti
        elif pyynto == "feeling lucky":
            print(random.choice(lista))

        #Kruuna ja klaava peli
        elif pyynto == "peli":
           rahaa += kruunavaiklaava()

        #Kauppa, missä voit ostaa tavaraa rahalla
        elif pyynto == "kauppa":
            rahaa, reppu = kauppa(rahaa, reppu)

        #Varasto, missä voit katsoo tavaroanne mitä ostit kaupasta
        elif pyynto == "reppu":
            varasto(rahaa, reppu)
             
        #Sammuttaa ohjelman
        elif pyynto == "loppu":
            print ("Kiitos kun pelasit")
            break

        #Tulee virhe jos käyttäjä antaa muu kun pääohjemassa annettiin
        else:
            print("ERROR!")