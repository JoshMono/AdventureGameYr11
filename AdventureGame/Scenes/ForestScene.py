import pygame
import all_classes
import random

class ForestScene:
    
    def _main_(player, screen):
        
        # Init Images
        background_image = pygame.image.load("Assets/VillageMapNew.png").convert()
        pick_up_image = pygame.image.load("Assets/Big_pickup96x.png")
        
        # Init Objects
        enemy = all_classes.Enemy((800,800))
        barrier_1 = all_classes.Barrier((72,42,1), (4991, 1), (1254,754) )
        sword = all_classes.Item('sword', (1800,800))
        
        camera = all_classes.Camera(background_image)
        wood_list = []
        for i in range(10):
            wood_list.append(all_classes.Item('wood', (random.randint(800,4000),random.randint(800, 3000))))
        
        # Init Groups
        all_sprites_group = pygame.sprite.Group()
        collision_group = pygame.sprite.Group()
        item_group = pygame.sprite.Group()
        enemy_group = pygame.sprite.Group()
        


        # Adding To Groupd
        all_sprites_group.add(sword)
        all_sprites_group.add(enemy)
        
        all_sprites_group.add(barrier_1)
        all_sprites_group.add(player)
        for i in wood_list:
            all_sprites_group.add(i)
            item_group.add(i)
            
        enemy_group.add(enemy)
        item_group.add(sword)
        collision_group.add(barrier_1)
        


        player.rect.topleft = (4000,1500)

        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)
    
            pressed_keys = pygame.key.get_pressed()
    
   
            for event in pygame.event.get():
                if pressed_keys[pygame.K_ESCAPE]:
                    running = False
                    break

                if event.type == pygame.QUIT:
                    running = False
                    break
        
            ui_detection = player.update(pressed_keys, collision_group, item_group, screen, background_image, enemy_group)
            
            
            camera.custom_blit(all_sprites_group, background_image, player, screen)

            if ui_detection != None:
                if ui_detection[0] == 'item':
                    pos = ui_detection[1].offset_pos
                    screen.blit(pick_up_image, pos)
                    
                elif ui_detection[0] == 'wood':
                    pos = ui_detection[1].offset_pos
                    screen.blit(pick_up_image, pos)
                    
                
                    

            
            pygame.display.flip()
            screen.fill((50, 157, 168))
   
   
        pygame.quit()