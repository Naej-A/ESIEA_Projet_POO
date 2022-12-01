import sample.Deck as Deck
import sample.GAMEPHASE as GAMEPHASE
import  pygame

class Scene():
    SCREEN_HEIGHT = 700
    SCREEN_WIDTH = 1000
    def __init__(self):
        self.listButton = Deck.Deck(False)
        self.backGround = pygame.transform.scale(pygame.image.load("../ressources/backGround.png"), (int(Scene.SCREEN_WIDTH), int(Scene.SCREEN_HEIGHT + 2)))
        self.timer = None
        self.gamePhase = None
        self.screen = pygame.display.set_mode((Scene.SCREEN_WIDTH, Scene.SCREEN_HEIGHT))



    def printAllButton(self):
        return None

    def chooseScene(self, game):
        self.screen.blit(self.backGround, (0, -1))
        if game.gamePhase.name == GAMEPHASE.GAMEPHASE.TAVERN.name:
            self.drawSceneTavern(game)
        elif game.gamePhase.name == GAMEPHASE.GAMEPHASE.SETTING.name:
            self.drawSceneSetting(game)
        elif game.gamePhase.name == GAMEPHASE.GAMEPHASE.FIGHT.name:
            self.drawSceneFight(game)


    def drawSceneTavern(self, game):

        return None
    def drawSceneSetting(self, game):
        return None
    def drawSceneFight(self, game):
        return None

