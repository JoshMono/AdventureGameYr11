import pygame

from Scenes.ForestScene import ForestScene


class MainMenu:
	def _main_(player, screen):
		class Button():
			def __init__(self, position, scale):
				self.width = scale[0] #image.get_width()
				self.height = scale[1] #image.get_height()
				self.surf = pygame.Surface(scale)
				self.surf.fill((1, 255, 255)) # Colour
				self.rect = self.surf.get_rect()
				self.rect.topleft = (position[0] - self.width / 2, position[1])
				self.clicked = False

			def draw(self):
				screen.blit(self.surf, (self.rect.x, self.rect.y))
	
		button = Button((400,400), (200,50))
		clock = pygame.time.Clock()
		
		b = True

		while b:
			a = button.draw()
			
			pressed_keys = pygame.key.get_pressed()
    
   
			for event in pygame.event.get():
				if pressed_keys[pygame.K_ESCAPE]:
					b = False

				if event.type == pygame.QUIT:
					b = False
					
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					if button.rect.collidepoint(pos):
						ForestScene._main_(player, screen)
			
			
			print(button.rect)
			pygame.display.flip()
			screen.fill((50, 157, 168))
			clock.tick(60)