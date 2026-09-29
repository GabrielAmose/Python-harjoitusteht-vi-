import random

#Moduuli 9. Luokka, olio ja alustaja, Tehtävä 1
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0 , kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    #Moduuli 9. Luokka, olio ja alustaja, Tehtävä 2
    #Tarkistaa audon kiihtyvyys
    def kiihtyvyys(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
            
        if self.nopeus < 0:
            self.nopeus = 0

    #Moduuli 9. Luokka, olio ja alustaja, Tehtävä 3
    #Lisää kuljetettu matka (km/h * tunti)
    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.nopeus * tuntimäärä


#Moduuli 10. Assosiaatio, Tehtävä 4
class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_km):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_km = pituus_km
        self.autojen_lista = []

    def tunti_kuluu(self, auto):
        auto.kiihtyvyys(random.randint(-10, 15))
        auto.kulje(1)

    def tulosta_tilanne(self, lista, numero):
        print("")
        print(f"Auto {numero + 1}: {lista.rekisteritunnus}")
        print(f"Huippunopeus: {lista.huippunopeus}")
        print(f"Kokonaismatka: {lista.kuljettu_matka}")

    def kilpailu_ohi(self, pituus, auto, voittaja):
        if auto >= pituus:
            print(f"Voittaja on {voittaja}")
            return True

#moduuli 11. Periytyminen, Tehtävä 2
class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, nopeus = 0 , kuljettu_matka = 0):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus, nopeus, kuljettu_matka)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki, nopeus = 0 , kuljettu_matka = 0):
        self.bensatankkki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus, nopeus, kuljettu_matka)


'''      
#Moduuli 9. Luokka, olio ja alustaja, Tehtävä 1
auto1 = Auto("AHT-396", 160)

print(f"auto 1: Rekisteritunnus: {auto1.rekisteritunnus}")
print(f"Huippunopeus: {auto1.huippunopeus}")
print(f"nopeus: {auto1.nopeus}")
print(f"Kuljettu matka: {auto1.kuljettu_matka}")


#Moduuli 9. Luokka, olio ja alustaja, Tehtävä 2
auto2 = Auto("JFU-285", 130)

auto2.kiihtyvyys(30)
auto2.kiihtyvyys(70)
auto2.kiihtyvyys(50)
print(f"Audon nopeus: {auto2.nopeus} km/h")

auto2.kiihtyvyys(-200)
print(f"Auto teki hätäjarrutus: {auto2.nopeus} km/h")


#Moduuli 9. Luokka, olio ja alustaja, Tehtävä 3
auto3 = Auto("OQP-951", 170, 100, 1700)

auto3.kulje(3)
print(auto3.kuljettu_matka)
'''

'''
#Moduuli 9. Luokka, olio ja alustaja, Tehtävä 4
lista = []
end = False
for x in range(10):
    
    kilpailja = Auto(f"ABC-{x + 1}", random.randint(100, 200))
    lista.append(kilpailja)


while True:
    for i in range(10):
        lista[i].kiihtyvyys(random.randint(-10, 15))
        lista[i].kulje(1)
        if lista[i].kuljettu_matka >= 10000:
            print(f"VOITTAJA ON {lista[i].rekisteritunnus}!")
            end = True
            break
    if end == True:
        break

print("")
print("**Lopputulos**")
for i in range(10):
    print("")
    print(f"Auto {i + 1}: {lista[i].rekisteritunnus}")
    print(f"Huippunopeus: {lista[i].huippunopeus}")
    print(f"Kokonaismatka: {lista[i].kuljettu_matka}") 
'''

'''
#moduuli 10. Assosiaatio, Tehtävä 4
k = Kilpailu("Suuri Romuralli", 8000)
end = False
for i in range(10):
    k.autojen_lista.append(Auto(f"ABC-{i + 1}", random.randint(100, 200)))

print(f"Tervettuloa {k.kilpailun_nimi}")

while end != True:
    for i in range(len(k.autojen_lista)):
        k.tunti_kuluu(k.autojen_lista[i])

        end = k.kilpailu_ohi(k.pituus_km, k.autojen_lista[i].kuljettu_matka, k.autojen_lista[i].rekisteritunnus)
        if end == True:
            break

print("**Lopputulos**")
for i in range(len(k.autojen_lista)):
    k.tulosta_tilanne(k.autojen_lista[i], i)
'''

#moduuli 11. Periytyminen, Tehtävä 2
sahko = Sahkoauto("SAH-294", 180, 52.5)
poltto = Polttomoottoriauto("POL-932", 165, 32.3)

sahko.kiihtyvyys(100)
poltto.kiihtyvyys(104)

sahko.kulje(3)
poltto.kulje(3)

print(f"Sähköaudon kuljettu matka: {sahko.kuljettu_matka}")
print(f"Polttomoottoriaudon kuljettu matka: {poltto.kuljettu_matka}")