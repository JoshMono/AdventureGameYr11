import pygame
import pygame.image

pygame.init()
screen_width = 1920
screen_height = 1280
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill((0, 0, 0))

background = pygame.image.load("MapForest.png").convert()

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
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

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.floor_rect = background.get_rect(topleft = (-1000,-600))

    def custom_blit(self):
        self.offset.x = player.rect.centerx - screen_width // 2
        self.offset.y = player.rect.centery - screen_height // 2

        background_offset_pos = self.floor_rect.topleft - self.offset

        screen.blit(background, background_offset_pos)

        for sprite in all_sprites_group:
            offset_pos = sprite.rect.topleft - self.offset
            screen.blit(sprite.surf, offset_pos)


player = Player()
clock = pygame.time.Clock()
running = True
camera = Camera()
all_sprites_group = pygame.sprite.Group()

all_sprites_group.add(player)

while running:
    clock.tick(60)
    
    pressed_keys = pygame.key.get_pressed()
   
    for event in pygame.event.get():
        if pressed_keys[pygame.K_ESCAPE]:
            running = False

        if event.type == pygame.QUIT:
            running = False
        
    player.update(pressed_keys)
    
    camera.custom_blit()
    pygame.display.flip()
    screen.fill((50, 157, 168))
   
   
pygame.quit()