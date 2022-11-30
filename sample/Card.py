
class Card(object):
    def __init__(self):
        self.deck = []
        self.deck = []
        self.attack = 0
        self.gamePhase = None
        self.name = ""
        self.race = None
        self.level = 0
        self.currentHealthPoint = 0
        self.healthPoint = 0
        self.description = ""
        
    # Start of user code -> properties/constructors for Card class

    # End of user code
    def doEffect(self):
        # Start of user code protected zone for doEffect function body
        raise NotImplementedError
        # End of user code	
    def attack(self, target):
        # Start of user code protected zone for attack function body
        self.healthPoint -= target.attack
        target.healthPoint -= self.attack
        # End of user code	
    # Start of user code -> methods for Card class

    # End of user code

