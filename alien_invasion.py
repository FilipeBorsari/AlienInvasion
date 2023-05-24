import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf




def run_game():

    #Inicializa o jogo e cria objeto pra tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption('Alien Invasion') 

    #Cria uma Espaço Nave
    ship = Ship(ai_settings, screen)

    #Cria Grupo para armazenar projeteis
    bullets = Group()

    #cria um Grupo para aliens
    aliens = Group()

    #cria a frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Inicia Laço principal do jogo:
    while True:
        
        gf.check_events(ai_settings, screen, ship, aliens, bullets)
        ship.update()
        bullets.update()
        
        #Apagar projeteis que passam da tela
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, ship, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
                
        

run_game()