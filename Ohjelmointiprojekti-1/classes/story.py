import json

class Story:
    def __init__(self):
        self.selected_options = []
        self.glass = False

    def bottle(self):
        while True:
            print("------------------------------")
            bott = jsonfile("bottle")
            print(bott["text"])
            print("------------------------------")
            print("1. Metal bottle")
            print("2. Glass bottle")
            inp = input()
            print("------------------------------")

            if inp == "1" or inp == "2":
                self.selected_options.append(inp)
                opt = bott["choice"]
                if inp == "2":
                    self.glass = True
                print(opt[inp])
                break

            else:
                print("ERROR!!!")

    def raccoon(self):
        while True:
            racc = jsonfile("raccoon")
            print(racc["text"])
            print("------------------------------")
            print("1. Feed him so that he leaves")
            print("2. Ignore it and continue building the tent")
            inp = input()
            print("------------------------------")

            if inp == "1" or inp == "2":
                self.selected_options.append(inp)
                opt = racc["choice"]
                print(opt[inp])
                break

            else:
                print("ERROR!!!")

    def bird(self):
        while True:
            bird = jsonfile("bird")
            print(bird["text"])
            print("------------------------------")
            print("1. feed it")
            print("2. ignore it")
            inp = input()
            print("------------------------------")

            if inp == "1" or inp == "2":
                self.selected_options.append(inp)
                opt = bird["choice"]
                print(opt[inp])
                break

            else:
                print("ERROR!!!")

    def deer(self):
        while True:
            deer = jsonfile("deer")
            if self.glass == True:
                print(deer["textglass"])
            print(deer["text"])
            print("------------------------------")
            print("1. no")
            print("2. yes")  
            inp = input()  
            print("------------------------------")

            if inp == "1" or inp == "2":
                self.selected_options.append(inp)
                opt = deer["choice"]
                print(opt[inp])
                break

            else:
                print("ERROR!!!")

    def bear(self):
        while True:
            bear = jsonfile("bear")
            print(bear["text"])
            print("------------------------------")
            print("1. scare it")
            print("2. ignore it and hope it doesnt eat you")    
            print("3. get out of there and come back tomorrow")    
            inp = input()
            print("------------------------------")

            if inp == "1" or inp == "2" or inp == "3":
                self.selected_options.append(inp)
                opt = bear["choice"]
                print(opt[inp])
                break

            else:
                print("ERROR!!!")

    def clean(self):
        while True:           
            clea = jsonfile("clean")

            #Different text wil be printed, depending on the options the player selected on the raccoon() and bear()
            if self.selected_options[1] == "1" and self.selected_options[4] == "2":
                print(clea["textrac"])

            elif self.selected_options[1] == "2" and self.selected_options[4] == "3":
                print(clea["textcar"])

            elif self.selected_options[1] == "1" and self.selected_options[4] == "3":
                print(clea["textraccar"])

            else:
                print(clea["textno"])

            print("------------------------------")
            print("1. Nope, i just wanna go home")
            print("2. Of course, its the right thing to do")
            inp = input()
            print("------------------------------")

            if inp == "1" or inp == "2":
                self.selected_options.append(inp)
                opt = clea["choice"]
                print(opt[inp])
                print("------------------------------")
                break

            else:
                print("ERROR!!!")

#Selecting text from the storytext.json file
def jsonfile(section):

    with open("Ohjelmointiprojekti-1\\textfiles\\storytext.json", "r") as file:
        story = json.load(file)
    scene = story["story"]
    return scene[section]