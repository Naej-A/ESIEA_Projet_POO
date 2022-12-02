import pygame


# button class
class Button():
    pygame.font.init()
    police = pygame.font.Font("sample/arial.ttf", 25)
    def __init__(self, name, x, y, image, scale, card):
        self.name = name
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.card = card

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        if self.card:
            image_texte = Button.police.render(str(self.card.attack), True, (255, 0, 0))
            surface.blit(image_texte, (self.rect.x + 5, self.rect.y + self.rect.width))
            image_texte = Button.police.render(str(self.card.currentHealthPoint), True, (0, 155, 0))
            surface.blit(image_texte, (self.rect.x + 62, self.rect.y + self.rect.width))

        return action
