import random
import time

import pygame

import sample.Player as Player
import sample.Tavern as Tavern
import sample.GAMEPHASE as GAMEPHASE
import sample.Scene as Scene
class Game(object):
    def __init__(self):
        self.maxFieldCard = 4
        self.gamePhase = None
        self.turnNumber = 0
        self.playerHuman = Player.Player()
        self.playerIA = Player.Player()
        self.tavern = Tavern.Tavern()
        self.scene = Scene.Scene()
        
    # Start of user code -> properties/constructors for Game class
    def startGame(self):
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
            self.scene.chooseScene(self)
            while nextButtonNotPressed:
                test = self.scene.findButtonByName("refresh")
                if test.draw(self.scene.screen):
                    # On en est la (bouton affiché mais ça crash encore wesh)
                    print("knkj")
                    self.tavern.refreshTavernHuman(self.playerHuman)

                # for button in  self.scene.findAllButtonByName("sellCard"):
                #     if button.draw(self.scene.screen):
                #         print("bknjl,k")
                #         self.playerHuman.sellCard(button.card, self.tavern)



                # if buyCard:
                #     self.playerHuman.buyCard()
                # if nextButton:
                #     nextButtonNotPressed = False
                pygame.display.update()

            #Phase setting
            self.gamePhase = GAMEPHASE.GAMEPHASE.SETTING
            self.playerIA.playSettingPhase(self)
            nextButtonNotPressed = True
            while nextButtonNotPressed:
                # if playCard:
                #     self.playerHuman.playCard()
                # if nextButton:
                #     self.playerHuman.fieldCardList.doAllEffect(self)
                #     self.playerIA.fieldCardList.doAllEffect(self)
                    nextButtonNotPressed = False
            #Phase fighting
            self.gamePhase = GAMEPHASE.GAMEPHASE.FIGHT
            firstPlayer, secondPlayer = self.chooseOrder()
            self.combatPhase(firstPlayer, secondPlayer)
            self.playerIA.turnCounter += 1
            self.playerHuman.turnCounter += 1




    def combatPhase(self,firstPlayer,secondPlayer):
        counterFirstPlayer = 0
        counterSecondPlayer = 0
        while len(firstPlayer.fieldCardList.cardList) > 0 and len(secondPlayer.fieldCardList.cardList) > 0:
            # attaque du first player
            if counterFirstPlayer >= len(firstPlayer.fieldCardList.cardList):
                counterFirstPlayer = 0

            firstPlayerCardTemp, secondPlayerCardTemp = firstPlayer.fieldCardList[counterFirstPlayer].attack(
                self.chooseTarget(secondPlayer.fieldCardList))
            if firstPlayerCardTemp.currentHealthPoint <= 0 :
                firstPlayer.fieldCardList.changeCardToOtherDeck(firstPlayerCardTemp, firstPlayer.handCardList)
            if secondPlayerCardTemp.currentHealthPoint <= 0:
                firstPlayer.fieldCardList.changeCardToOtherDeck(secondPlayerCardTemp, firstPlayer.handCardList)

            counterFirstPlayer += 1

            # attaque du second player

            if counterSecondPlayer >= len(secondPlayer.fieldCardList.cardList):
                counterSecondPlayer = 0

            secondPlayerCardTemp, firstPlayerCardTemp = secondPlayer.fieldCardList[counterSecondPlayer].attack(
                self.chooseTarget(firstPlayer.fieldCardList))
            if firstPlayerCardTemp.currentHealthPoint <= 0:
                firstPlayer.fieldCardList.changeCardToOtherDeck(firstPlayerCardTemp, firstPlayer.handCardList)
            if secondPlayerCardTemp.currentHealthPoint <= 0:
                firstPlayer.fieldCardList.changeCardToOtherDeck(secondPlayerCardTemp, firstPlayer.handCardList)

            counterSecondPlayer += 1

        for card in secondPlayer.fieldCardList:
                firstPlayer.healthPoint -= card.level
        for card in secondPlayer.fieldCardList:
                secondPlayer.fieldCardList.changeCardToOtherDeck(card, secondPlayer.handCardList)
        for card in firstPlayer.fieldCardList:
                secondPlayer.healthPoint -= card.level
        for card in firstPlayer.fieldCardList:
                firstPlayer.fieldCardList.changeCardToOtherDeck(card, firstPlayer.handCardList)

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

