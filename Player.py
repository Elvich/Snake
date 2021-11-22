import pygame
import Main

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(Main.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (Main.WIDTH / 2, Main.HEIGHT / 2)
        
        
    def update(self):
        self.rect.x += 5
        if self.rect.left > Main.WIDTH:
            self.rect.right = 0