import sample.cards.Card as Card

class CardLifeSteal(Card):

    def __init__(self, name, race, gamePhase, level, attack, maxHealthPoint, description):
        Card.Card.__init__(self, name, race, gamePhase, level, attack, maxHealthPoint, description)

    def attack(self, targetCard):
        """
        attack the target card and heal the damage
        :param targetCard: the card to attack
        :return: [self, targetCard]
        """
        if self.hasShield:
            self.hasShield = False
        else:
            self.currentHealthPoint -= targetCard.attackCard
        if targetCard.hasShield:
            targetCard.hasShield = False
        else:
            targetCard.currentHealthPoint -= self.attack
            if self.currentHealthPoint > 0:
                self.currentHealthPoint += self.attack
        return self, targetCard