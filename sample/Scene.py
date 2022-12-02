import sample.Deck as Deck
import sample.GAMEPHASE as GAMEPHASE
import pygame
import sample.button as button

class Scene():
    SCREEN_HEIGHT = 700
    SCREEN_WIDTH = 1000
    def __init__(self):
        self.listButton = []
        self.backGround = pygame.transform.scale(pygame.image.load("ressources/backGround.png"), (int(Scene.SCREEN_WIDTH), int(Scene.SCREEN_HEIGHT + 2)))
        self.timer = None
        self.screen = pygame.display.set_mode((Scene.SCREEN_WIDTH, Scene.SCREEN_HEIGHT))



    def chooseScene(self, game):
        self.screen.blit(self.backGround, (0, -1))
        if game.gamePhase.name == GAMEPHASE.GAMEPHASE.TAVERN.name:
            self.drawSceneTavern(game)
        elif game.gamePhase.name == GAMEPHASE.GAMEPHASE.SETTING.name:
            self.drawSceneSetting(game)
        elif game.gamePhase.name == GAMEPHASE.GAMEPHASE.FIGHT.name:
            self.drawSceneFight(game)


    def drawSceneTavern(self, game):
        self.listButton = []
        tempImg = pygame.image.load('ressources/refresh.png').convert_alpha()
        refresh = button.Button("refresh", 5.9 * Scene.SCREEN_WIDTH / 10, 2 * Scene.SCREEN_HEIGHT / 13, tempImg, 3, None)
        self.listButton.append(refresh)
        #Ajouté le bouton pour passer à la phase suivant, puis, passer à la phase suivante
        counter = 0
        for card in game.tavern.listCardShopHuman.cardList:
            tempImg = pygame.image.load('ressources/AUBIN_Jean_Pierre_card.png').convert_alpha()
            buyCard = button.Button("buyCard",  Scene.SCREEN_WIDTH/2 + counter - ( 90 + 1.5 * tempImg.get_width() / 10), 5 * Scene.SCREEN_HEIGHT / 11 - tempImg.get_height() / 10, tempImg, 0.1, card)
            self.listButton.append(buyCard)
            counter += tempImg.get_width() / 10 + 100
        counter = 0
        for card in game.playerHuman.handCardList.cardList:
            tempImg = pygame.image.load('ressources/CRISON_Franck_card.png').convert_alpha()
            sellCard = button.Button("sellCard", (Scene.SCREEN_WIDTH - tempImg.get_width()) / 11 + counter, Scene.SCREEN_HEIGHT - (tempImg.get_height() / 10 + (Scene.SCREEN_WIDTH - tempImg.get_width()) / 11), tempImg, 0.1, card)
            self.listButton.append(sellCard)
            counter += (Scene.SCREEN_WIDTH - tempImg.get_width()) / 11 + tempImg.get_width() / 10


        # start_img = pygame.image.load('exit_btn.png').convert_alpha()
        # sellCard = button.Button("sellCard", 500, 300, start_img, 0.5)
        # self.listButton.append(sellCard)

    def drawSceneSetting(self, game):
        self.screen.blit(self.backGround, (0, -1))
    def drawSceneFight(self, game):
        self.screen.blit(self.backGround, (0, -1))

    def findButtonByName(self, name):
        for button in self.listButton:
            if button.name == name:
                return button
        return None


    def findAllButtonByName(self, name):
        listTemp = []
        for button in self.listButton:
            if button.name == name:
                listTemp.append(button)
        return listTemp

