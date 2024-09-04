import pygame

class ForestScene:
    
    def _main_(player, screen):
        
        class Camera(pygame.sprite.Group):
            def __init__(self):
                super().__init__()
                self.offset = pygame.math.Vector2()
                self.floor_rect = background.get_rect(topleft = (-1000,-600))

            def custom_blit(self, all_sprites_group):
                self.offset.x = player.rect.centerx - player.screen_width // 2
                self.offset.y = player.rect.centery - player.screen_height // 2

                background_offset_pos = self.floor_rect.topleft - self.offset

                screen.blit(background, background_offset_pos)

                for sprite in all_sprites_group:
                    offset_pos = sprite.rect.topleft - self.offset
                    screen.blit(sprite.surf, offset_pos)

        class Enviourment(pygame.sprite.Sprite):
            def __init__(self, image, size, position):
                pygame.sprite.Sprite.__init__(self)
                self.surf = pygame.Surface(size)
                self.surf.fill((1, 255, 255)) # Colour
                self.rect = self.surf.get_rect()
                self.rect.topleft = position
        
                screen.blit(self.surf, position)
    
        background = pygame.image.load("MapForest.png").convert()
        tree = Enviourment(None, (50,100), (150,150))
        
        clock = pygame.time.Clock()
        running = True
        camera = Camera()
        all_sprites_group = pygame.sprite.Group()
        enviourment_group = pygame.sprite.Group()

        all_sprites_group.add(player)
        all_sprites_group.add(tree)

        enviourment_group.add(tree)

        while running:
            clock.tick(60)
    
            pressed_keys = pygame.key.get_pressed()
    
   
            for event in pygame.event.get():
                if pressed_keys[pygame.K_ESCAPE]:
                    running = False

                if event.type == pygame.QUIT:
                    running = False
        
            player.update(pressed_keys, enviourment_group)
    
            camera.custom_blit(all_sprites_group)
            pygame.display.flip()
            screen.fill((50, 157, 168))
   
   
        pygame.quit()