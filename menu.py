import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280,720))

bg_surface = pygame.image.load('background.png').convert()
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.blit(bg_surface,(0,0))
	pygame.display.update()
	clock.tick(120)
