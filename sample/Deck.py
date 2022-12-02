import sample.cards.Card as Card
# import sample.cards.CardShield as CardShield
# import sample.cards.CardHPBoost as CardHPBoost
# import sample.cards.CardLifeSteal as CardLifeSteal
import sample.RACE as RACE
import sample.GAMEPHASE as GAMEPHASE

class Deck(object):
    def __init__(self, isEmpty):
        if isEmpty:
            self.cardList = []
        else:
            self.cardList = Deck.initAllCard()

    def doAllEffect(self, game):
        """
        do the effect of all the card in the deck
        :param game: the running game
        :return: None
        """
        for card in self.cardList:
            card.doEffect(game, self)
        return None
    def addCard(self, card):
        """
        add card to the deck
        :param card: the card to add
        :return: return the added card
        """
        self.cardList.append(card)
        return card

    def findCardByName(self, name):
        """
        find a card int the deck by his name
        :param name: the name of the card to search
        :return: a card with the same name or none if nothing found
        """
        for card in self.cardList:
            if card.name == name:
                return card
        return None

    def findCard(self, cardToSearch):
        """
        find a card object in the deck
        :param cardToSearch: the card to search
        :return: a card or None if nothing found
        """
        for card in self.cardList:
            if card == cardToSearch:
                return card
        return None

    def findCardHigherLevel(self):
        """
        find one of the highest level card in the deck
        :return:
        """
        if len(self.cardList) == 0:
            return None
        cardLevelMax = self.cardList[0]
        for card in self.cardList:
            if card.level > cardLevelMax.level:
                cardLevelMax = card
        return cardLevelMax

    def findCardLowerLevel(self):
        """
        find one of the lowest level card
        :return: return one card of the lowest level or none list length is 0
        """
        if len(self.cardList) == 0:
            return None
        cardLevelMin = self.cardList[0]
        for card in self.cardList:
            if card.level < cardLevelMin.level:
                cardLevelMin = card
        return cardLevelMin

    def removeCard(self,card):
        """
        remove a card from a deck
        :param card: the card object to remove
        :return: the removed card
        """
        cardTemp = self.findCard(card)
        if cardTemp:
            self.cardList.remove(card)
        return cardTemp

    def changeCardToOtherDeck(self, card, deckDestination):
        """
        send a card from the deck to a destination deck
        :param card: the card to send
        :param deckDestination: the deck that will receive the card
        :return: the searched card
        """
        tempCard = self.removeCard(card)
        if tempCard:
            deckDestination.addCard(tempCard)
        return tempCard

    @staticmethod
    def initAllCard():
        """
        init all card
        :return: the list of cards
        """
        # name, race, gamePhase, level, attack, maxHealthPoint, description
        tempList = []
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "AUBIN_Jean_Pierre_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", "CRISON_Franck_card.png", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))

        return tempList