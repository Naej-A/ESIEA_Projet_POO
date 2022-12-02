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

    def findCardLowerLevel(self, cardList):
        if len(cardList) == 0:
            return None
        cardLevelMin = cardList[0]
        for card in cardList.cardList:
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
        tempCard = self.removeCard(card)
        if tempCard:
            deckDestination.addCard(tempCard)
        return tempCard

    @staticmethod
    def initAllCard():
        # name, race, gamePhase, level, attack, maxHealthPoint, description
        tempList = []
        tempList.append(Card.Card("Michel", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("Michel", RACE.RACE.Beast, GAMEPHASE.GAMEPHASE.NONE, 1, 2, 1, "Mi ingénieur mi bête, Michel est d'uné férocité métodique irréprochable"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        tempList.append(Card.Card("VéroNIQUE", RACE.RACE.Mech, GAMEPHASE.GAMEPHASE.NONE, 1, 1, 5, "NIQUE"))
        return tempList