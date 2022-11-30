
class Deck(object):
    def __init__(self, isEmpty):
        if isEmpty:
            self.cardList = []
        else:
            self.cardList = Deck.initAllCard()

    def doAllEffect(self):
        for card in self.cardList:
            card.doEffect()

    def doAllEffectOfGamePhase(self, gamePhase):
        for card in self.cardList:
            if card.gamePhase == gamePhase:
                card.doEffect()

    def addCard(self, card):
        self.cardList.append(card)
        return card

    def findCardByName(self, name):
        for card in self.cardList:
            if card.name == name:
                return card
        return None

    def findCard(self, cardToSearch):
        for card in self.cardList:
            if card == cardToSearch:
                return card
        return None

    def removeCard(self,card):
        cardTemp = self.findCard(card)
        if cardTemp:
            self.cardList.remove(card)
        return cardTemp

    def changeCardToOtherDeck(self, card, deck):
        tempCard = self.removeCard(card)
        if tempCard:
            deck.addCard(tempCard)
        return tempCard

    @staticmethod
    def initAllCard():
        return []