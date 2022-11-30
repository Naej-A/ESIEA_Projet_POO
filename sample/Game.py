import random
import sample.Player as Player
import sample.Tavern as Tavern
import sample.GAMEPHASE as GAMEPHASE
class Game(object):
    def __init__(self):
        self.maxFieldCard = 4
        self.gamePhase = None
        self.turnNumber = 0
        self.playerHuman = Player.Player()
        self.playerIA = Player.Player()
        self.tavern = Tavern.Tavern()
        
    # Start of user code -> properties/constructors for Game class
    def startGame(self):
        #Initiallisation
        # Phase achat
        # Phase posage
        # Phase combat
        while self.playerHuman.healthPoint > 0 and self.playerIA.healthPoint > 0:
            self.turnNumber += 1
            self.playerHuman.setGold(self)
            self.playerIA.setGold(self)
            self.tavern.refreshTavernHuman(self.playerHuman)
            self.tavern.refreshTavernIA(self.playerIA)
            #Phase tavern
            self.gamePhase = GAMEPHASE.GAMEPHASE.TAVERN
            self.playerIA.playTavernPhase(self.tavern)
            nextButtonNotPressed = True
            while nextButtonNotPressed:
                if refreshTavern:
                    self.tavern.refreshTavernHuman(self.playerHuman)
                if sellCard:
                    self.playerHuman.sellCard()
                if buyCard:
                    self.playerHuman.buyCard()
                if nextButton:
                    nextButtonNotPressed = False
            self.gamePhase = GAMEPHASE.GAMEPHASE.SETTING
            self.playerIA.playSettingPhase(self.tavern)
            nextButtonNotPressed = True
            while nextButtonNotPressed:
                if egr:





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
        while self.playerHuman.monsterNumber > 0 and self.playerIA.monsterNumber > 0:
            firstPlayer.fieldCardList[1].attack(self.chooseTarget(secondPlayer))
        # End of user code	
    def chooseOrder(self):
        # Start of user code protected zone for chooseBeginer function body
        if random.randint(1, 2) == 1:
            firstPlayer = self.playerHuman
            secondPlayer = self.playerIA
        else:
            firstPlayer = self.playerIA
            secondPlayer = self.playerHuman
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

