#Different ending outcomes
class Ending:
    def good_ending(self, player):
        print("Master camper ending")
        player.add_ending("master")

    def feeder_ending(self, player):
        print("Feeder ending")
        player.add_ending("feeder")

    def amature_ending(self, player):
        print("Amature camper ending")
        player.add_ending("amature")

    def worst_ending(self, player):
        print("Worst camper ending")
        player.add_ending("worst")

    def killed(self, player):
        print("You lose ending")
        player.add_ending("bear")