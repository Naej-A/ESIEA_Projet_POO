import random
class Game(object):
    def __init__(self, maxFieldCard, player1, player2):
        self.maxFieldCard = maxFieldCard
        self.gamePhase = None
        self.turnNumber = 0
        self.player1 = player1
        self.player2 = player2
        
    # Start of user code -> properties/constructors for Game class
    def startGame(self):
        while self.player1 > 0 and self.player2 > 0:
            self.turnNumber += 1
            # Phase de tavern

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
        firstPlayer, secondPlayer = self.chooseOrder()
        while self.player1.monsterNumber > 0 and self.player2.monsterNumber > 0:
            firstPlayer.fieldCardList[1].attack(self.chooseTarget(secondPlayer))
        # End of user code	
    def chooseOrder(self):
        # Start of user code protected zone for chooseBeginer function body
        if random.randint(1, 2) == 1:
            firstPlayer = self.player1
            secondPlayer = self.player2
        else:
            firstPlayer = self.player2
            secondPlayer = self.player1
        return firstPlayer, secondPlayer
        # End of user code	
    def chooseTarget(self, opponentField):
        # Start of user code protected zone for chooseTarget function body
        possibleTarget = []
        for iCard in opponentField:
            if iCard.healthPoint > 0:
                possibleTarget.append(iCard)
        return random.choice(possibleTarget)


        # End of user code	
    # Start of user code -> methods for Game class

    # End of user code

