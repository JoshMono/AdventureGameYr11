import pygame
import all_classes

class ForestScene:
    
    def _main_(player, screen):
        
        
    
        background_image = pygame.image.load("Assets/VillageMapNew.png").convert()
        pick_up_image = pygame.image.load("Assets/Big_pickup96x.png")
        barrier_1 = all_classes.Barrier((72,42,1), (4991, 1), (1254,754) )
        sword = all_classes.Item('sword', (0,0))

        clock = pygame.time.Clock()
        running = True
        camera = all_classes.Camera(background_image)
        all_sprites_group = pygame.sprite.Group()
        collision_group = pygame.sprite.Group()
        item_group = pygame.sprite.Group()



        #all_sprites_group.add(top_green_barrier)
        all_sprites_group.add(sword)
        all_sprites_group.add(barrier_1)
        all_sprites_group.add(player)


        item_group.add(sword)
        collision_group.add(barrier_1)
        
        player.rect.topleft = (-500, 200)

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
        
            ui_detection = player.update(pressed_keys, collision_group, item_group)
            
            camera.custom_blit(all_sprites_group, background_image, player, screen)

            if ui_detection != None:
                if ui_detection[0] == 'item':
                    print(ui_detection[1].offset_pos)
                    pos = ui_detection[1].offset_pos
                    screen.blit(pick_up_image, pos)


            pygame.display.flip()
            screen.fill((50, 157, 168))
   
   
        pygame.quit()