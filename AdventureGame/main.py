import pygame
import pygame.image
from Scenes.ForestScene import ForestScene
from Scenes.MainMenu import MainMenu

pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill((0, 0, 0))



class Main:
    class PlayerSprite(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.surf = pygame.Surface((25, 75))
            self.surf.fill((255, 255, 255))
            self.rect = self.surf.get_rect()
        
        def update(self, pressed_keys, enviourment_group):
            speed = 3
            if pressed_keys[pygame.K_LSHIFT]:
                speed = 5
        
            if pressed_keys[pygame.K_a]:
                self.rect.move_ip(-1*speed, 0)
                collide = pygame.sprite.spritecollide(self, enviourment_group, False)
                if collide != []:
                    self.rect.move_ip(speed, 0)

            if pressed_keys[pygame.K_w]:
                self.rect.move_ip(0, -1*speed)
                collide = pygame.sprite.spritecollide(self, enviourment_group, False)
                if collide != []:
                    self.rect.move_ip(0, speed)

            if pressed_keys[pygame.K_s]:
                self.rect.move_ip(0, speed)
                collide = pygame.sprite.spritecollide(self, enviourment_group, False)
                if collide != []:
                    self.rect.move_ip(0, -1*speed)

            if pressed_keys[pygame.K_d]:
                self.rect.move_ip(speed, 0)
                collide = pygame.sprite.spritecollide(self, enviourment_group, False)
                if collide != []:
                    self.rect.move_ip(-1*speed, 0)
            

    class Player(PlayerSprite):
        def __init__(self, screen_height, screen_width):
            super().__init__()
            self.screen_height = screen_height
            self.screen_width = screen_width

    
    player = Player(screen_height, screen_width)
    MainMenu._main_(player, screen)
Main()