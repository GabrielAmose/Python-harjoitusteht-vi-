from classes import Story, Ending

def game(player):
    stor = Story()
    endin = Ending()

    #these are coming from the Story() class
    stor.bottle()
    stor.raccoon()
    stor.bird()
    stor.deer()
    stor.bear()
    if stor.selected_options[4] == "1":
        print("------------------------------")
        endin.killed(player)
        return
    
    stor.clean()

    if stor.selected_options == ["1", "2", "2", "1", "3", "2"]:
        endin.good_ending(player)

    elif stor.selected_options == ["2", "1", "1", "2", "2", "1"]:
        endin.worst_ending(player)

    elif stor.selected_options[1] == "1" and stor.selected_options[2] == "1":
        endin.feeder_ending(player)

    else:
        endin.amature_ending(player)