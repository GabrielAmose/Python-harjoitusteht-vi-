from .game import game

def main_menu(player):
    print(f"Hello {player.name}")
    
    while True:
        print("------------------------------")
        print(f"Welcome to SURVIVING CAMP")
        print(f"Endings found: {len(player.ending)}/5")
        print("------------------------------")
        print("1. Start game")    
        print("2. Quit game")
        inp = input()

        if inp == "1":
            game(player)

            #Updates the save file
            with open("Ohjelmointiprojekti-1\\textfiles\\save.txt", "w") as s:
                s.write(player.name + "\n")
                s.write(str(player.age) + "\n")

                for i in player.ending:
                    s.write(i + "\n")
            

        elif inp == "2":
            print("thank you for playing my game!")
            break

        else:
            print("ERROR!!!")
