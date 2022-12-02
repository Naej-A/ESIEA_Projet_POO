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
            self.gamePhase = GAMEPHASE.GAMEPHASE.TAVERN
            self.playerIA.playTavernPhase(self.tavern)
            nextButtonNotPressed = True
            while nextButtonNotPressed:
                self.playerHuman.gold = 10 # SUPPRIMER ça !!!
                self.scene.chooseScene(self)
                if self.scene.findButtonByName("refresh").draw(self.scene.screen):
                    print("refresh")
                    self.tavern.refreshTavernHuman(self.playerHuman)
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
                clock.tick(2000)
                for event in pygame.event.get():
                    # quit game
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
            #Phase setting
            self.gamePhase = GAMEPHASE.GAMEPHASE.SETTING
            self.playerIA.playSettingPhase(self)
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
                clock.tick(2000)
                for event in pygame.event.get():
                    # quit game
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
            #Phase fighting
            # Faire les effets
            self.gamePhase = GAMEPHASE.GAMEPHASE.FIGHT
            self.scene.chooseScene(self)
            time.sleep(5)
            firstPlayer, secondPlayer = self.chooseOrder()
            self.combatPhase(firstPlayer, secondPlayer)
            self.playerIA.turnCounter += 1
            self.playerHuman.turnCounter += 1

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
            # attaque du first player
            if counterFirstPlayer >= len(firstPlayer.fieldCardList.cardList):
                self.scene.chooseScene(self)
                time.sleep(1.5)
                counterFirstPlayer = 0
            self.scene.chooseScene(self)
            time.sleep(1.5)
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
            self.scene.chooseScene(self)
            time.sleep(1.5)
            secondPlayerCardTemp, firstPlayerCardTemp = secondPlayer.fieldCardList[counterSecondPlayer].attack(
                self.chooseTarget(firstPlayer.fieldCardList))
            if firstPlayerCardTemp.currentHealthPoint <= 0:
                firstPlayer.fieldCardList.changeCardToOtherDeck(firstPlayerCardTemp, firstPlayer.handCardList)
            if secondPlayerCardTemp.currentHealthPoint <= 0:
                firstPlayer.fieldCardList.changeCardToOtherDeck(secondPlayerCardTemp, firstPlayer.handCardList)

            counterSecondPlayer += 1

        for card in secondPlayer.fieldCardList.cardList:
                firstPlayer.healthPoint -= card.level
        for card in secondPlayer.fieldCardList.cardList:
                secondPlayer.fieldCardList.changeCardToOtherDeck(card, secondPlayer.handCardList)
        for card in firstPlayer.fieldCardList.cardList:
                secondPlayer.healthPoint -= card.level
        for card in firstPlayer.fieldCardList.cardList:
                firstPlayer.fieldCardList.changeCardToOtherDeck(card, firstPlayer.handCardList)

    def fight(self):
        # Start of user code protected zone for fight function body
        firstPlayer, secondPlayer = self.chooseOrder()
        while self.playerHuman.monsterNumber > 0 and self.playerIA.monsterNumber > 0:
            firstPlayer.fieldCardList[1].attack(self.chooseTarget(secondPlayer))
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
        for iCard in opponentField:
            if iCard.healthPoint > 0:
                possibleTarget.append(iCard)
        return random.choice(possibleTarget)


        # End of user code	
    # Start of user code -> methods for Game class

    # End of user code

