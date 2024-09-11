import pygame
import random
import asyncio

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        #self.width = image.get_width()
        #self.height = image.get_height()
        #self.image = image
        self.width = 40
        self.height = 40
        self.surf = pygame.Surface((self.width, self.height))
        self.image = self.surf
        self.rect = self.surf.get_rect()
        swing_rect = pygame.sprite.Sprite()
        swing_rect.width = self.width
        swing_rect.height = self.height
        swing_rect.surf = pygame.Surface((swing_rect.width, swing_rect.height))
        swing_rect.rect = swing_rect.surf.get_rect()
        swing_rect.surf.fill((0,0,0))
        self.swing_cooldown = 0
        
        self.swing_rect = swing_rect

        
    def update(self, pressed_keys, collision_group, item_group, screen, background, enemy_group):
        speed = 3

        if pressed_keys[pygame.K_LSHIFT]:
            speed = 5
        
        
        if pressed_keys[pygame.K_a]:
                        
                
            self.rect.move_ip(-1*speed, 0)
            collide = pygame.sprite.spritecollide(self, collision_group, False)
            if collide != []:
                self.rect.move_ip(speed, 0)
                
            if self.inventory['sword']:
                self.swing_rect.rect.topleft = (self.rect.left - self.swing_rect.width, self.rect.top)
                a = pygame.sprite.spritecollide(self.swing_rect, item_group, False)
                
                print(self.rect.topleft)
                print(self.swing_rect.rect.topleft)
                
                print(" ")

                if a != []:
                    for i in a:
                        print(i)
           
                

        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0, -1*speed)
            collide = pygame.sprite.spritecollide(self, collision_group, False)
            if collide != []:
                self.rect.move_ip(0, speed)
                
           

        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0, speed)
            collide = pygame.sprite.spritecollide(self, collision_group, False)
            if collide != []:
                self.rect.move_ip(0, -1*speed)
           

        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(speed, 0)
            collide = pygame.sprite.spritecollide(self, collision_group, False)
            
            if collide != []:
                self.rect.move_ip(-1*speed, 0)
                
        if self.swing_cooldown == 0:

            if pressed_keys[pygame.K_SPACE]:
                if self.inventory['sword']:
                    self.swing_sword(enemy_group)
                    
        else:
            self.swing_cooldown -= 1

        if pygame.sprite.spritecollide(self, item_group, False):
            item = pygame.sprite.spritecollide(self, item_group, False)
            if pressed_keys[pygame.K_e]:
                item[0].pick_up(self)

            return ("item", item[0])

        return None
    
    def swing_sword(self, enemy_group):
        self.swing_cooldown = 40
        a = pygame.sprite.spritecollide(self.swing_rect, enemy_group, False)
        print(self.swing_rect.rect.topleft)
        
        
        if a != []:
            for i in a:
                i.surf.fill((random.randrange(1,240),random.randrange(1,240),random.randrange(1,240)))


            



class Player(PlayerSprite):
    def __init__(self, screen_height, screen_width, image):
        super().__init__(image)
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.health = 100
        self.inventory = {
                'sword': False,
                'wood': 0
            }
     
class Enemy(pygame.sprite.Sprite):
     def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.width = 40
        self.height = 40
        self.surf = pygame.Surface((self.width, self.height))
        self.image = self.surf
        self.rect = self.surf.get_rect()
        self.surf.fill((25,120,244))
        self.rect.topleft = pos


class Camera(pygame.sprite.Group):
        def __init__(self, background):
            super().__init__()
            self.offset = pygame.math.Vector2()
            self.floor_rect = background.get_rect(topleft = (0,0))

        def custom_blit(self, all_sprites_group, background, player, screen):
            self.offset.x = player.rect.centerx - player.screen_width // 2
            self.offset.y = player.rect.centery - player.screen_height // 2

            background_offset_pos = self.floor_rect.topleft - self.offset

            screen.blit(background, background_offset_pos)

            for sprite in all_sprites_group:
                offset_pos = sprite.rect.topleft - self.offset
                sprite.offset_pos = offset_pos
                screen.blit(sprite.image, offset_pos)

                

class Enviourment(pygame.sprite.Sprite):
    def __init__(self, image, size, position):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface(size)
        self.surf.fill((0,0,0)) # Colour
        if image == None:
            self.image = self.surf
        else:
            self.image = image
        self.rect = self.surf.get_rect()
        self.rect.topleft = position

class Barrier(pygame.sprite.Sprite):
    def __init__(self, colour, size, position):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface(size)
        self.surf.fill(colour) # Colour
                
        self.image = self.surf
                
        self.rect = self.surf.get_rect()
        self.rect.topleft = position


class Item(pygame.sprite.Sprite):
    def __init__(self, item, position):
        self.item = item
        pygame.sprite.Sprite.__init__(self)
        if self.item == 'sword':
            self.image = pygame.image.load("Assets/BigSword96x.png")
            
        elif self.item == 'wood':
            self.image = pygame.image.load("Assets/Wood96x.png")
            
        else:
            self.image = self.surf
                        
        self.surf = pygame.Surface((96,96))
        self.rect = self.surf.get_rect()
        self.rect.topleft = position

    def pick_up(self, player):
        self.kill()
        if self.item == 'sword':
            player.inventory['sword'] = True
            player.surf.fill((255,255,255))
            
        if self.item == 'wood':
            player.inventory['wood'] += 1
            player.surf.fill((100,100,255))
        


