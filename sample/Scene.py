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
        # self.screen.blit(self.backGround, (0, -1))
        if game.gamePhase.name == GAMEPHASE.GAMEPHASE.TAVERN.name:
            self.drawSceneTavern(game)
        elif game.gamePhase.name == GAMEPHASE.GAMEPHASE.SETTING.name:
            self.drawSceneSetting(game)
        elif game.gamePhase.name == GAMEPHASE.GAMEPHASE.FIGHT.name:
            self.drawSceneFight(game)


    def drawSceneTavern(self, game):
        self.listButton = []


        start_img = pygame.image.load('ressources/start_btn.png').convert_alpha()
        refresh = button.Button("refresh", 800, 300, start_img, 0.5, None)
        self.listButton.append(refresh)
        counter = 0
        for card in game.tavern.listCardShopHuman.cardList:
            start_img = pygame.image.load('ressources/exit_btn.png').convert_alpha()
            sellCard = button.Button("sellCard", 400 + counter, 300, start_img, 0.5, card)
            self.listButton.append(sellCard)
            counter += 100



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

