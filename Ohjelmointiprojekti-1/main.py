from functions import main_menu
from classes import Player

#If this game has a save file in the textfilrs folder
try:
    #Loads the save file
    with open("Ohjelmointiprojekti-1\\textfiles\\save.txt", "r") as s:
        name = s.readline().strip()
        age = s.readline().strip()
        character = Player(name, age)

        for i in s:
            character.ending.add(i.strip())

    main_menu(character)

#if this is played for the first time
except:
    name = input("What is your name?: ")

    while True:
        try:
            age = int(input("How old are you?: "))
            break
    
        except ValueError:
            print("ERROR!!!")

    if age < 12:
        print("Im sorry but you are too young to play this game, try again once you are old enough.")

    else:
        #Creates a new save file
        with open("Ohjelmointiprojekti-1\\textfiles\\save.txt", "w") as s:
            s.write(name + "\n")
            s.write(str(age) + "\n")
        character = Player(name, age)
        main_menu(character)