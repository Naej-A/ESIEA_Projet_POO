
class Card(object):
    def __init__(self, name, imageName, race, gamePhase, level, attack, maxHealthPoint, description):
        self.name = name
        self.imageName = imageName
        self.race = race
        self.gamePhase = gamePhase
        self.level = level
        self.attack = attack
        self.maxHealthPoint = maxHealthPoint
        self.currentHealthPoint = maxHealthPoint
        self.description = description
        self.hasShield = False
        
    # Start of user code -> properties/constructors for Card class

    # End of user code
    def doEffect(self, game, fieldCardList):
        """
        do the effect of a card
        :param game: the actual game
        :param fieldCardList: the field where the effect takes place
        :return: None
        """
        return
    def attackCard(self, targetCard):
        """
        attack and inflict damage to another car if she has no shield
        :param targetCard: the card to target
        :return: himself and the targetedCard [himself,targetedCard]
        """
        if self.hasShield:
            self.hasShield = False
        else:
            self.currentHealthPoint -= targetCard.attack
        if targetCard.hasShield:
            targetCard.hasShield = False
        else:
            targetCard.currentHealthPoint -= self.attack
        return self, targetCard


