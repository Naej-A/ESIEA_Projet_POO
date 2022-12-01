import random
import sample.Deck as Deck
class Tavern(object):
    def __init__(self):
        self.maxLevel = 4
        self.deck = Deck.Deck(False)
        self.listCardShopHuman = Deck.Deck(True)
        self.listCardShopIA = Deck.Deck(True)

        
    # Start of user code -> properties/constructors for Tavern class

    # End of user code
    def refreshTavernHuman(self, player):
        # Start of user code protected zone for refreshTavern function body
        if player.gold >= 1:
            player.gold -= 1
            for card in self.listCardShopHuman.cardList:
                print(card)
                self.listCardShopHuman.changeCardToOtherDeck(card, self.deck)
            counter = 0
            while counter < 3:
                card = random.choice(self.deck.cardList)
                if player.tavernLevel >= card.level:
                    self.deck.changeCardToOtherDeck(card, self.listCardShopHuman)
                    counter += 1
        return None
    def refreshTavernIA(self, player):
        # Start of user code protected zone for refreshTavern function body
        if player.gold >= 1:
            player.gold -= 1
            for card in self.listCardShopIA.cardList:
                self.deck.changeCardToOtherDeck(card, self.listCardShopIA)
            counter = 0
            while counter < 3:
                card = random.choice(self.deck.cardList)
                if player.tavernLevel >= card.level:
                    self.listCardShopIA.changeCardToOtherDeck(card, self.deck)
                    counter += 1
        return None
    # Start of user code -> methods for Tavern class

    # End of user code

