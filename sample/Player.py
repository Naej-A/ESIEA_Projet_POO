import random

import sample.Deck as Deck
class Player(object):
    def __init__(self):
        self.turnCounter = 0
        self.tavernLevel = 1
        self.gold = 0
        self.handCardList = Deck.Deck(True)
        self.fieldCardList = Deck.Deck(True)
        self.healthPoint = 20
    # Start of user code -> properties/constructors for Player class

    # End of user code
    def buyCardHuman(self, card, tavern):
        """
        Human buy a card from the tavern
        :param card: the card to buy
        :param tavern: the tavern from witch the player buy a card
        :return: None
        """
        # Start of user code protected zone for buyCard function body
        if self.gold >= 3 and len(self.handCardList.cardList) < 10:
            self.gold -= 3
            tavern.listCardShopHuman.changeCardToOtherDeck(card, self.handCardList)
        return None
    def buyCardIA(self, card, tavern):
        """
        AI player buy a card from the tavern
        :param card: the card to buy
        :param tavern: the tavern from witch the player buy a card
        :return: None
        """
        # Start of user code protected zone for buyCard function body
        if self.gold >= 3 and len(self.handCardList.cardList) < 10:
            self.gold -= 3
            tavern.listCardShopIA.changeCardToOtherDeck(card, self.handCardList)
        return None
        # End of user code	
    def levelUpTavern(self, tavern):
        """
        level up the tavern
        :param tavern: the tavern to level up
        :return: None
        """
        # Start of user code protected zone for levelUp function body
        levelUpCost = 5 - self.turnCounter
        if self.tavernLevel < tavern.maxLevel and self.gold >= levelUpCost:
            self.tavernLevel += 1
            self.gold -= levelUpCost
            self.turnCounter = 0
        return None
        # End of user code	
    def setGold(self, game):
        # Start of user code protected zone for levelUp function body
        self.gold = min(game.turnNumber + 3, 11)
        # End of user code	
    def sellCard(self, card, tavern):
        # Start of user code protected zone for sellCard function body
        self.gold += 1
        self.handCardList.changeCardToOtherDeck(card, tavern.deck)
        # End of user code	
    def playCard(self, card, game):
        # Start of user code protected zone for playCard function body
        if len(self.fieldCardList.cardList) < game.maxFieldCard:
            self.handCardList.changeCardToOtherDeck(card, self.fieldCardList)
        return None
        # End of user code	
    # Start of user code -> methods for Player class
    def monsterNumber(self):
        return len(self.fieldCardList.cardList)

    # End of user code
    def playTavernPhase(self, tavern):
        """
        The AI player play the tavern phase
        :param tavern: the tavern the AI will buy from
        :return: None
        """
        if random.randint(0, 1):
            self.levelUpTavern(tavern)
        if len(self.handCardList.cardList) > 4:
            self.sellCard(self.handCardList.findCardLowerLevel(), tavern)
        self.buyCardIA(tavern.listCardShopIA.findCardHigherLevel(), tavern)
        if len(self.handCardList.cardList) > 4:
            self.sellCard(self.handCardList.findCardLowerLevel(), tavern)
        tavern.refreshTavernIA(self)
        self.buyCardIA(tavern.listCardShopIA.findCardHigherLevel(), tavern)
        self.buyCardIA(tavern.listCardShopIA.findCardHigherLevel(), tavern)
        if len(self.handCardList.cardList) > 4:
            self.sellCard(self.handCardList.findCardLowerLevel(),tavern)
        tavern.refreshTavernIA(self)
        if len(self.handCardList.cardList) > 4:
            self.sellCard(self.handCardList.findCardLowerLevel(),tavern)
        self.buyCardIA(tavern.listCardShopIA.findCardHigherLevel(), tavern)

    def playSettingPhase(self, game):
        """
        The AI play the setting phase
        :param game: the game running
        :return: None
        """
        for i in range(game.maxFieldCard):
            self.playCard(self.handCardList.findCardHigherLevel(), game)
