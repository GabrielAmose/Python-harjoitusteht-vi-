leiviskat = input ("Kirjoita leiviskät: ")
naulat = input ("Kirjoita naulat: ")
luodit = input ("Kirjoita luodit: ")

mluodit = float(luodit) * 13.3
mnaulat = float(naulat) * (13.3 * 32)
mleiviskat = float(leiviskat) * (13.3 * 32 * 20)

massa = mleiviskat + mnaulat + mluodit
kgmassa = massa / 1000

gmassa = (massa - (int(kgmassa) * 1000))

print("Massa nykymittojen mukaan: ")
print(str(int(kgmassa)) + " kg ja " + str(gmassa) + " g")