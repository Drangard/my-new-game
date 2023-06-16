
import pygame
import pygame.math

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((16,32))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 4
        self.gravity = 0.2
        self.jump_speed = -5.5
        self.max_jump_height = 100
        self.is_jumping = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        #elif keys[pygame.K_]:
         #  pass
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            if self.direction.y == 0:
                if not self.is_jumping:
                    self.is_jumping = True
                    self.jump()
        
        if not keys[pygame.K_SPACE]:
            self.is_jumping = False



    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed


    def update(self):  
        self.get_input()
        
