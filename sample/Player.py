import random

import sample.Deck as Deck
class Player(object):
    def __init__(self):
        self.turnCounter = 0
        self.tavernLevel = 0
        self.gold = 0
        self.handCardList = Deck.Deck(True)
        self.fieldCardList = Deck.Deck(True)
        self.healthPoint = 20
    # Start of user code -> properties/constructors for Player class

    # End of user code
    def buyCard(self, card, tavern):
        # Start of user code protected zone for buyCard function body
        if self.gold >= 3 and len(self.handCardList.cardList) < 10:
            self.gold -= 3
            tavern.listCardShop.changeCardToOtherDeck(card, self.handCardList)
        return None
        # End of user code	
    def levelUpTavern(self, tavern):
        # Start of user code protected zone for levelUp function body
        levelUpCost = 5 - self.turnCounter
        if self.tavernLevel < tavern.maxLevel and self.gold >= 5 - levelUpCost:
            self.tavernLevel += 1
            self.gold -= levelUpCost
            self.turnCounter = 0
        return None
        # End of user code	
    def setGold(self, game):
        # Start of user code protected zone for levelUp function body
        self.gold = max(game.turnNumber + 2, 10)
        # End of user code	
    def sellCard(self, card, tavern):
        # Start of user code protected zone for sellCard function body
        self.gold += 1
        self.handCardList.changeCardToOtherDeck(card, tavern.deck)
        # End of user code	
    def playCard(self, card):
        # Start of user code protected zone for playCard function body
            self.fieldCardList.changeCardToOtherDeck(card, self.handCardList)
        # End of user code	
    # Start of user code -> methods for Player class
    def monsterNumber(self):
        return len(self.fieldCardList.cardList)

    # End of user code
    def playTavernPhase(self, tavern):
        if random.randint(0, 1):
            self.levelUpTavern(tavern)
        if len(self.handCardList.cardList) > 4:
            self.sellCard(self.handCardList.findCardLowerLevel(self.handCardList))
        self.buyCard(tavern.listCardShopIA.findCardHigherLevel(tavern.listCardShopIA), tavern)
        if len(self.handCardList.cardList) > 4:
            self.sellCard(self.handCardList.findCardLowerLevel(self.handCardList))
        tavern.refreshTavernIA()
        self.buyCard(tavern.listCardShopIA.findCardHigherLevel(tavern.listCardShopIA), tavern)
        self.buyCard(tavern.listCardShopIA.findCardHigherLevel(tavern.listCardShopIA), tavern)
        if len(self.handCardList.cardList) > 4:
            self.sellCard(self.handCardList.findCardLowerLevel(self.handCardList))
        tavern.refreshTavernIA()
        if len(self.handCardList.cardList) > 4:
            self.sellCard(self.handCardList.findCardLowerLevel(self.handCardList))
        self.buyCard(tavern.listCardShopIA.findCardHigherLevel(tavern.listCardShopIA), tavern)


