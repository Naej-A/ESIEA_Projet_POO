import Card

class CardShieldl(Card):

    def __init__(self, name, race, gamePhase, level, attack, maxHealthPoint, description):
        Card.Card.__init__(self, name, race, gamePhase, level, attack, maxHealthPoint, description)
        self.hasShield = True
