import pygame


class MainMenu:
	def _main_(player, screen):
		class Button():
			def __init__(self, position, scale):
				self.width = 200 #image.get_width()
				self.height = 50 #image.get_height()
				self.surf = pygame.Surface(scale)
				self.surf.fill((1, 255, 255)) # Colour
				self.rect = self.surf.get_rect()
				self.rect.topleft = position
				self.clicked = False

			def draw(self):
				action = False
				pos = pygame.mouse.get_pos()

				
				

				screen.blit(self.surf, (self.rect.x, self.rect.y))

				return action
	
		button = Button((400,640), (200,50))
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
        
			
			pos = pygame.mouse.get_pos()
			
			print(button.rect)
			print(pos)
			if button.rect.collidepoint(pos):
				print("Here")
				
			pygame.display.flip()
			screen.fill((50, 157, 168))
			screen.blit(button.surf, (button.rect.x, button.rect.y))
			clock.tick(60)