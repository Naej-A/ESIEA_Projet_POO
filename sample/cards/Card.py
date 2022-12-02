
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
        return
    def attack(self, targetCard):
        if self.hasShield:
            self.hasShield = False
        else:
            self.currentHealthPoint -= targetCard.attack
        if targetCard.hasShield:
            targetCard.hasShield = False
        else:
            targetCard.currentHealthPoint -= self.attack
        return self, targetCard


