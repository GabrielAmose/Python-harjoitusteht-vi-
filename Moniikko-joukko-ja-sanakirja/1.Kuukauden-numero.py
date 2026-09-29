vuodenaika = {"12":"Talvi", "1":"Talvi", "2":"Talvi",
              "3":"Kevät", "4":"Kevät", "5":"Kevät",
              "6":"Kesä", "7":"Kesä", "8":"Kesä",
              "9":"Syksy", "10":"Syksy", "11":"Syksy"}

kuukausi = input("Anna joku kuukauden numero: ")

if kuukausi in vuodenaika:
    print(f"kuukausi {kuukausi} on vuodenajassa {vuodenaika[kuukausi]}")