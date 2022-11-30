
class Card(object):
    def __init__(self, name, race, gamePhase, level, attack, maxHealthPoint, description):
        self.name = name
        self.race = race
        self.gamePhase = gamePhase
        self.level = level
        self.attack = attack
        self.maxHealthPoint = maxHealthPoint
        self.currentHealthPoint = maxHealthPoint
        self.description = description
        
    # Start of user code -> properties/constructors for Card class

    # End of user code
    def doEffect(self):
        return
    def attack(self, targetCard):
        self.currentHealthPoint -= targetCard.attack
        targetCard.healthPoint -= self.attack

