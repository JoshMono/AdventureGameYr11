import pygame

from Scenes.ForestScene import ForestScene


class MainMenu:
	def _main_(player, screen):
		class Button():
			def __init__(self, image, position, scale):
				self.width = scale[0] #image.get_width()
				self.height = scale[1] #image.get_height()
				self.surf = pygame.Surface(scale)
				self.image = image
				self.rect = self.surf.get_rect()
				self.rect.topleft = (position[0] - self.width / 2, position[1])
				self.clicked = False

			def draw(self):
				screen.blit(self.image, (self.rect.x, self.rect.y))
	
		start_image = pygame.image.load("Assets/StartImage.png").convert()
		button = Button(start_image, (player.screen_width/2,player.screen_height/2), (250,70))
		clock = pygame.time.Clock()
		
		running = True

		while running:
			button.draw()
			
			pressed_keys = pygame.key.get_pressed()
    
   
			for event in pygame.event.get():
				if pressed_keys[pygame.K_ESCAPE]:
					running = False
					break

				if event.type == pygame.QUIT:
					running = False
					break
					
			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				if button.rect.collidepoint(pos):
					running = False
					ForestScene._main_(player, screen)
					break

			pygame.display.flip()
			screen.fill((50, 157, 168))
			clock.tick(60)