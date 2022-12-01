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
        for card in self.cardList:
            card.doEffect(game, self)

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
    def findCardHigherLevel(self, deck):
        if len(deck.cardList) == 0:
            return None
        cardLevelMax = deck.cardList[0]
        for card in deck.cardList:
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