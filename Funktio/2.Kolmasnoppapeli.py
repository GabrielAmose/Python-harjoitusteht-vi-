import random

#Heittää noppaa
def noppa_heitto(max):
    num = random.randint(1, max)
    return num

#pyytää käyttäjältä maksimi tahkoo nopassa
monta = int(input("Montako tahkoo haluat nopassa on: "))

while True:

    num2 = noppa_heitto(monta)
    print(num2)

    #Jos noppa on kutonen
    if num2 == monta:
        break