import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ representação alien"""

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
    
        #carregar imagem do alien
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #inicia cada novo alien próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height
        

    def blitme(self):
        """ desenha o alien """
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """ Irá retornar True se atingir a borda"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    def update(self):
        """ Move o Alien para direita ou esquerda"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

