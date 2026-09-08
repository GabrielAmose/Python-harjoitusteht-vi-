#Laskee pizzan hinta per cm^2
def pizzaarvo(halkaisia, hinta):
    pizpin = 3.141 * halkaisia ** 2 / 4
    pizhin = hinta / pizpin
    return pizhin

#pyytää käyttäjältä kahden pizzan halkaisia(cm) ja hinta(€)
print("Kysytään teiltä 2 pizzaa ja kerron teille mikä on parempi arvo")
pizzahal1 = float(input("Mikä on ensimmäisen pizzan halkaisia (cm): "))
pizzahin1 = float(input("Ja sen hinta (€): "))
pizzahal2 = float(input("Mikä on toisen pizzan halkaisia (cm): "))
pizzahin2 = float(input("Ja sen hinta (€): "))

#Pyytää funktiolta pizzan yksikköhinta
pizza1 = pizzaarvo(pizzahal1, pizzahin1)
pizza2 = pizzaarvo(pizzahal2, pizzahin2)

#Jos ensimmäisen pizzan yksikköhinta on alemppi
if pizza1 < pizza2:
    text = "Ensimmäinen pizza in parempi diili"

#Jos toisen pizzan yksikköhinta on alemppi
elif pizza1 > pizza2:
    text = "Toinen pizza in parempi diili"

#Jos molempien Pizzan yksikköhinta ovat samat
else:
    text = "Molemmmat pizzat ovat sama diili"

print(text)