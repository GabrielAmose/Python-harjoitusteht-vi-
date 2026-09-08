#Laskee gallonamäärä litraksi
def gallon_nappain(gal):
    
    litra = gal * 3.785
    return litra

#Pyytää käyttäjältä gallonamäärä
num = float(input("Kuinka monta gallonaa: "))

#Tulostaa gallonan ja litran määrä
print(f"{num} gallonaa on {gallon_nappain(num)} litraa")