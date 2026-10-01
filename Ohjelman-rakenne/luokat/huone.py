class Huone:
    def __init__(self, huoneen_nimi, esine):
        self.huoneen_nimi = huoneen_nimi
        self.esine = esine

    def tyhjenna_huone(self, tyhja):
        self.esine = tyhja
