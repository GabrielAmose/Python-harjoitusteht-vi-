with open("Tiedostonkäsittely\\intro.txt", "r", encoding='utf-8') as intro:
    print(intro.read())

with open("Tiedostonkäsittely\\ohjeet.txt", "r", encoding='utf-8') as rules:
    print(rules.read()) 



class Player:
    def __init__(self, name, held_in_hand):
        self.name = name
        self.hold = held_in_hand

    def pickup(self, object):
        self.held == object


class Object:
    def __init__(self, name):
        self.name = name


stick = Object("stick")
ball = Object("Ball")
pillow = Object("pillow")

try:
    with open("Tiedostonkäsittely\\save.txt", "r") as nimi:
        name = nimi.readline().strip()
        item = nimi.readline().strip()
        player = Player(name, item)

#Jos ei ole save.txt
except:
    inp = input("what is your name?: ")
    with open("Tiedostonkäsittely\\save.txt", "w") as nimi:
        nimi.write(inp + "\n")
        nimi.write("none" + "\n")
        player = Player(inp, "none")

print(f"Hello {player.name}")

while True:
    print("-------------------")
    print(f"you are currently holding: {player.hold}")
    print("1. stick")
    print("2. ball")
    print("3. pillow")
    print("4. end game")

    inp = input("which one do you wanna pick up?: ")

    if inp == "1":
        player.hold = "stick"

    elif inp == "2":
        player.hold = "ball"

    elif inp == "3":
        player.hold = "pillow"

    elif inp == "4":
        print("thank you for playing my game")
        break

    else:
        print("ERROR!!!")

    with open("Tiedostonkäsittely\\save.txt", "w") as save:
        save.write(player.name + "\n")
        save.write(player.hold + "\n")
    