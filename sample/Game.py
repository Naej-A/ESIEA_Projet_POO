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
        """
        the function that will run the game
        :return: None
        """
        clock = pygame.time.Clock()
        while self.playerHuman.healthPoint > 0 and self.playerIA.healthPoint > 0:
            self.turnNumber += 1
            self.playerHuman.setGold(self)
            self.playerIA.setGold(self)
            self.tavern.refreshTavernHuman(self.playerHuman)
            self.tavern.refreshTavernIA(self.playerIA)
            #Phase tavern
            self.playerIA.playTavernPhase(self.tavern)
            print("main IA :")
            print(self.playerIA.handCardList.cardList)
            nextButtonNotPressed = True
            while nextButtonNotPressed:
                self.gamePhase = GAMEPHASE.GAMEPHASE.TAVERN
                self.scene.chooseScene(self)
                if self.scene.findButtonByName("refresh").draw(self.scene.screen):
                    print("refresh")
                    self.tavern.refreshTavernHuman(self.playerHuman)
                if self.scene.findButtonByName("levelUp").draw(self.scene.screen):
                    print("levelUp")
                    self.playerHuman.levelUpTavern(self.tavern)
                for button in self.scene.findAllButtonByName("buyCard"):
                    if button.draw(self.scene.screen):
                        print(button.card.name)
                        print(button.card)
                        self.playerHuman.buyCardHuman(button.card, self.tavern)
                for button in self.scene.findAllButtonByName("sellCard"):
                    if button.draw(self.scene.screen):
                        print(button.card.name)
                        print(button.card)
                        self.playerHuman.sellCard(button.card, self.tavern)
                if self.scene.findButtonByName("nextPhase").draw(self.scene.screen):
                    print("nextPhase")
                    nextButtonNotPressed = False
                pygame.display.update()
                clock.tick(200)
                for event in pygame.event.get():
                    # quit game
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
            #Phase setting
            self.gamePhase = GAMEPHASE.GAMEPHASE.SETTING
            self.playerIA.playSettingPhase(self)
            print("Terrain IA :")
            print(self.playerIA.fieldCardList.cardList)
            nextButtonNotPressed = True
            while nextButtonNotPressed:
                self.scene.chooseScene(self)
                for button in self.scene.findAllButtonByName("playCard"):
                    if button.draw(self.scene.screen):
                        self.playerHuman.playCard(button.card, self)
                for button in self.scene.findAllButtonByName("takeCardBack"):
                    if button.draw(self.scene.screen):
                        print("On peut pas retirer de cartes connard !")
                if self.scene.findButtonByName("nextPhase").draw(self.scene.screen):
                    print("nextPhase")
                    nextButtonNotPressed = False
                pygame.display.update()
                clock.tick(200)
                for event in pygame.event.get():
                    # quit game
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
            #Phase fighting
            # Faire les effets
            self.gamePhase = GAMEPHASE.GAMEPHASE.FIGHT
            print("entrée en gamephase fight")
            self.scene.chooseScene(self)
            for button in self.scene.findAllButtonByName("takeCardBack"):
                if button.draw(self.scene.screen):
                    print("On peut pas retirer de cartes connard !")
            pygame.display.update()
            print("time sleep 2")
            time.sleep(2)
            print("fin time sleep")
            firstPlayer, secondPlayer = self.chooseOrder()
            self.combatPhase(firstPlayer, secondPlayer)
            self.playerIA.turnCounter += 1
            self.playerHuman.turnCounter += 1

        if self.playerHuman.healthPoint > self.playerIA.healthPoint:
            print("Victory !")
        else:
            print("Defete")
        print("End of the game")

    def combatPhase(self, firstPlayer, secondPlayer):
        """
        automatically resolve the combat
        :param firstPlayer: the first player to attack
        :param secondPlayer: the second player to attack
        :return: None
        """
        counterFirstPlayer = 0
        counterSecondPlayer = 0
        while len(firstPlayer.fieldCardList.cardList) > 0 and len(secondPlayer.fieldCardList.cardList) > 0:
            if counterFirstPlayer >= len(firstPlayer.fieldCardList.cardList):
                counterFirstPlayer = 0
            self.scene.chooseScene(self)
            time.sleep(1.5)
            firstPlayerCardTemp, secondPlayerCardTemp = firstPlayer.fieldCardList.cardList[counterFirstPlayer].attackCard(self.chooseTarget(secondPlayer.fieldCardList))
            if firstPlayerCardTemp.currentHealthPoint <= 0:
                firstPlayerCardTemp.currentHealthPoint = firstPlayerCardTemp.maxHealthPoint
                firstPlayer.fieldCardList.changeCardToOtherDeck(firstPlayerCardTemp, firstPlayer.handCardList)
            if secondPlayerCardTemp.currentHealthPoint <= 0:
                secondPlayerCardTemp.currentHealthPoint = secondPlayerCardTemp.maxHealthPoint
                secondPlayer.fieldCardList.changeCardToOtherDeck(secondPlayerCardTemp, secondPlayer.handCardList)

            counterFirstPlayer += 1

            tempPlayer = firstPlayer
            firstPlayer = secondPlayer
            secondPlayer = tempPlayer
            tempCounter = counterFirstPlayer
            counterFirstPlayer = counterSecondPlayer
            counterSecondPlayer = tempCounter
            self.scene.chooseScene(self)
            pygame.display.update()
            for button in self.scene.findAllButtonByName("takeCardBack"):
                if button.draw(self.scene.screen):
                    print("On peut pas retirer de cartes connard !")

        temp = len(secondPlayer.fieldCardList.cardList)
        for index in range(temp):
                firstPlayer.healthPoint -= secondPlayer.fieldCardList.cardList[index].level
        temp = len(firstPlayer.fieldCardList.cardList)
        for index in range(temp):
                secondPlayer.healthPoint -= firstPlayer.fieldCardList.cardList[index].level
        temp = len(secondPlayer.fieldCardList.cardList)
        for i in range(temp):
                secondPlayer.fieldCardList.changeCardToOtherDeck(secondPlayer.fieldCardList.cardList[0], secondPlayer.handCardList)
        temp = len(firstPlayer.fieldCardList.cardList)
        for i in range(temp):
                firstPlayer.fieldCardList.changeCardToOtherDeck(firstPlayer.fieldCardList.cardList[0], firstPlayer.handCardList)

    def fight(self):
        # Start of user code protected zone for fight function body
        firstPlayer, secondPlayer = self.chooseOrder()
        while self.playerHuman.monsterNumber > 0 and self.playerIA.monsterNumber > 0:
            firstPlayer.fieldCardList[1].attackCard(self.chooseTarget(secondPlayer))
        # End of user code	
    def chooseOrder(self):
        """
        choose the first players to play between the human and the IA
        :return: [firstPlayer, secondPlayer]
        """
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
        """
        choose a random card to target
        :param opponentField: the deck where to choose the deck
        :return: card object to target
        """
        # Start of user code protected zone for chooseTarget function body
        possibleTarget = []
        for iCard in opponentField.cardList:
            if iCard.currentHealthPoint > 0:
                possibleTarget.append(iCard)
        return random.choice(possibleTarget)


        # End of user code	
    # Start of user code -> methods for Game class

    # End of user code

