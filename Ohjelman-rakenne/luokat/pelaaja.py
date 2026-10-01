
class Pelaaja:
    def __init__(self, pelaaja_nimi, sijainti):
        self.pelaaja_nimi = pelaaja_nimi
        self.sijainti = sijainti
        self.reppu = []

    def liiku(self, huoneet):
        while True:
            print("------------------------------")
            for i in range(len(huoneet)):
                if huoneet[i] != self.sijainti:
                    print(f"{i + 1}. {huoneet[i].huoneen_nimi}")
    
            pyynto = input("missä haluat mennä (laita pelkästään numero): ")

            if pyynto.isdigit():
                pyynto = int(pyynto) - 1

            else:
                print("ERROR!!!")
                continue

            if pyynto < 0 or pyynto > len(huoneet):
                print("ERROR!!!")
                continue

            else:
                self.sijainti = huoneet[pyynto]
                break

    def ota_esine(self, tyhja):
        if self.sijainti.esine != tyhja:
            self.reppu.append(self.sijainti.esine)
            self.sijainti.tyhjenna_huone(tyhja)
        else:
            print("Huoneessa ei ole mitään.")

    def tarkista_reppu(self):
        print("------------------------------")
        summa = 0.0
        for i in range(len(self.reppu)):
            print(f"{i + 1}. {self.reppu[i].esine_nimi}, Paino: {self.reppu[i].paino}g")
            summa += self.reppu[i].paino
            if i == len(self.reppu) - 1:
                print(f"Yhtenäinen paino: {summa}") 
        input("Takaisin (Enter): ")