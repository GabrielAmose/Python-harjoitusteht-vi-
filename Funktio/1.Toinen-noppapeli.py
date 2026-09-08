import random

#Heittää noppaa
def noppa_heitto():
    num = random.randint(1, 6)
    return num

while True:
    num2 = noppa_heitto()
    print(num2)

    #Jos noppa on kutonen
    if num2 == 6:
        break