def nykyinen_tilanne(pelaaja):
    print("------------------------------")
    print(f"Moi {pelaaja.pelaaja_nimi}!")
    print("**Päävalikoima**")
    print(f"Nykyinen sijainti: {pelaaja.sijainti.huoneen_nimi}")
    print(f"Esine: {pelaaja.sijainti.esine.esine_nimi}")
    print("1. Vaihda huonetta")
    print("2. Ottaa esineen")
    print("3. Tarkista reppu")
    print("4. Lopeta peli")

    pyynto = input("Valitse valikoimasta (Vain numero): ")
    return pyynto 