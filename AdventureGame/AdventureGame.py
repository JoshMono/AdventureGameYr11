import pygame

pygame.init()
screen_width = 512
screen_height = 512
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill((0, 0, 0))

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self.surf = pygame.Surface((25, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        
    def update(self, pressed_keys):
        print("jasdnjkasnjkasndjnas")
        if pressed_keys[pygame.K_a]:
            self.rect.move_ip(-5, 0)

        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0, -5)

        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0, 5)

        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(5, 0)
            print("Move")

class Player(PlayerSprite):
    def __init__(self):
        super().__init__()



player = Player()
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    
    pressed_keys = pygame.key.get_pressed()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    player.update(pressed_keys)
    
    screen.blit(player.surf, player.rect)
    pygame.display.flip()
    screen.fill((50, 157, 168))
    