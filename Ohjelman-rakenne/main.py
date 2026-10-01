from luokat import Pelaaja, huoneet, tyhja, nykyinen_tilanne

name = input("Mikä on teidän nimi: ")
hahmo = Pelaaja(name, huoneet[0])


while True:
    nyky = nykyinen_tilanne(hahmo)
    if nyky == "1":
        hahmo.liiku(huoneet)

    elif nyky == "2":
        hahmo.ota_esine(tyhja)

    elif nyky == "3":
        hahmo.tarkista_reppu()

    elif nyky == "4":
        print("------------------------------")
        print(f"Kiitos kun pelasit {hahmo.pelaaja_nimi}!")
        break

