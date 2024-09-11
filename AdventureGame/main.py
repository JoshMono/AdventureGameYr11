import pygame
import pygame.image
from Scenes.ForestScene import ForestScene
from Scenes.MainMenu import MainMenu
import all_classes

pygame.init()
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill((0, 0, 0))



class Main:
    

    image = pygame.image.load('Assets/BigSword96x.png')
    player = all_classes.Player(screen_height, screen_width, image)
    MainMenu._main_(player, screen)
Main()