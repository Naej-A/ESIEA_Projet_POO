import random
import sample.Deck as Deck
class Tavern(object):
    def __init__(self):
        self.maxLevel = 4
        self.deck = Deck.Deck(False)
        self.listCardShopp1 = Deck.Deck(True)
        self.listCardShopp2 = Deck.Deck(True)

        
    # Start of user code -> properties/constructors for Tavern class

    # End of user code
    def refreshTavernp1(self, player):
        # Start of user code protected zone for refreshTavern function body
        if player.gold >= 1:
            player.gold -= 1
            for card in self.listCardShopp1.cardList:
                self.deck.changeCardToOtherDeck(card, self.listCardShopp1)
            counter = 0
            while counter < 3:
                card = random.choice(self.deck.cardList)
                if player.tavernLevel >= card.level:
                    self.listCardShopp1.changeCardToOtherDeck(card, self.deck)
                    counter += 1
        return None
        # End of user code	
    # Start of user code -> methods for Tavern class

    # End of user code

