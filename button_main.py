import pygame
import sample.button as button
import sample.Game as Game
import sample.Scene as Scene
import sample.GAMEPHASE as GAMEPHASE

#create display window
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('../ressources/start_btn.png').convert_alpha()
exit_img = pygame.image.load('../ressources/exit_btn.png').convert_alpha()
# bg = pygame.image.load("../ressources/backGround.png").convert_alpha()


game = Game.Game()
game.gamePhase = GAMEPHASE.GAMEPHASE.TAVERN
scene = Scene.Scene()


#create button instances
start_button = button.Button("",100, 200, start_img, 0.8,None)
exit_button = button.Button("",450, 200, exit_img, 0.8,None)

#game loop
run = True
while run:

	# screen.fill((202, 228, 241))
	scene.chooseScene(game)
	if start_button.draw(screen):
		print('START')
	if exit_button.draw(screen):
		print('EXIT')
	# if game.gamePhase.name == GAMEPHASE.GAMEPHASE.TAVERN.name:
	# 	if Refresh.draw(screen):
	# 		print('Refresh')

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()

	pygame.display.update()
