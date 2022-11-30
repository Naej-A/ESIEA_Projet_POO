
class Game(object):
    def __init__(self, maxFieldCard, player1, player2):
        self.maxFieldCard = maxFieldCard
        self.gamePhase = None
        self.turnNumber = 0
        self.player1 = player1
        self.player2 = player2
        
    # Start of user code -> properties/constructors for Game class

    # End of user code
    def doEffect(self):
        # Start of user code protected zone for doEffect function body
        raise NotImplementedError
        # End of user code	
    def doAllEffect(self):
        # Start of user code protected zone for doAllEffect function body
        raise NotImplementedError
        # End of user code	
    def fight(self):
        # Start of user code protected zone for fight function body
        raise NotImplementedError
        # End of user code	
    def chooseBeginer(self):
        # Start of user code protected zone for chooseBeginer function body
        raise NotImplementedError
        # End of user code	
    def chooseTarget(self):
        # Start of user code protected zone for chooseTarget function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Game class

    # End of user code

