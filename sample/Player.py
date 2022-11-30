
class Player(object):
    def __init__(self):
        self.turnCounter = 0
        self.tavernLevel = 0
        self.tavern = []
        self.game = []
        self.gold = 0
        self.handCardList = None
        self.deck = None
        self.fieldCradList = None
        self.healthPoint = 0
        
    # Start of user code -> properties/constructors for Player class

    # End of user code
    def buyCard(self):
        # Start of user code protected zone for buyCard function body
        if self.gold >= 3:
            self.gold -= 3
        #WORK IN PROGESS
        # End of user code	
    def levelUp(self, tavern):
        # Start of user code protected zone for levelUp function body
        levelUpCost = 5 - self.turnCounter
        if self.tavernLevel > tavern.maxLevel and self.gold >= 5 - levelUpCost:
            self.tavernLevel += 1
        else:
            return None
        # End of user code	
    def setGold(self, game):
        # Start of user code protected zone for levelUp function body
        self.gold = max(game.turnNumber + 2, 10)
        # End of user code	
    def sellCard(self):
        # Start of user code protected zone for sellCard function body
        raise NotImplementedError
        # End of user code	
    def playCard(self):
        # Start of user code protected zone for playCard function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Player class

    # End of user code

