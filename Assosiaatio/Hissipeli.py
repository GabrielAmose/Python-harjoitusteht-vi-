class Hissi:
    def __init__(self, hissi_alin_kerros = 1, hissi_ylin_kerros = 5):
        self.alin = hissi_alin_kerros
        self.ylin = hissi_ylin_kerros
        self.nykyinen_kerros = self.alin


    def siirry_kerros(self, kohde):
        if kohde > self.ylin or kohde < self.alin:
            print(f"kerros {kohde} ei ole olemassa")

        elif kohde > self.nykyinen_kerros:
            while kohde != self.nykyinen_kerros:
                self.kerros_ylos()
                print(self.nykyinen_kerros)

        elif kohde < self.nykyinen_kerros:
            while kohde != self.nykyinen_kerros:
                self.kerros_alas()
                print(self.nykyinen_kerros)
                
    def kerros_ylos(self):
        self.nykyinen_kerros += 1

    def kerros_alas(self):
        self.nykyinen_kerros -= 1

class Talo:
    def __init__(self, hissi_maara, talo_alin_kerros = 1, talo_ylin_kerros = 5):
        self.alin_kerros = talo_alin_kerros
        self.ylin_kerros = talo_ylin_kerros
        self.hissi = hissi_maara
        self.hissejä = []
        for i in range(self.hissi):
            self.hissejä.append(Hissi())

    def ajaa_hissi(self, hissi, kohdekerros):
        hissi.siirry_kerros(kohdekerros)

    def palohalytys(self):
        for i in range(len(self.hissejä)):
            h = self.hissejä[i]
            h.siirry_kerros(1)


t = Talo(3)
t.ajaa_hissi(t.hissejä[0], 3)

t.ajaa_hissi(t.hissejä[1], 5)
t.ajaa_hissi(t.hissejä[2], 4)

t.palohalytys()

