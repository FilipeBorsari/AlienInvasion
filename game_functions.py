import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ responde ao pressionamento"""
    if event.key == pygame.K_RIGHT:
        #Move Nave para Direita
        ship.moving_right = True
        
    if event.key == pygame.K_LEFT:
        #Move Nave para Esquerda
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
        if len(bullets) < ai_settings.bullets_allowed:
            #Cria um novo projétil e adiciona no grupo de projeteis
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def get_number_rows(ai_settings, ship_height, alien_height):
    """ Número de aliens que cabem na tela """
    available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #cria um alien e posiciona na linha
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """ Cria uma frota completa de alien """
    #cria um alien e calcula o numero em uma linha 
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width) )
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #cria a frota de alien
    for row_number in range (number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
        

def check_keyup_events(event, ship):
    #Para de mover
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    #Para de mover               
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, aliens, bullets):
    """Responde teclado e mouse"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Atualiza a Tela"""
    screen.fill(ai_settings.bg_color)

    #Redesenha todos os projéteis atrás da espaçonave e dos aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Atualiza a posição dos projeteis e limpa projeteis antigos """
    bullets.update()  
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        check_bullet_alien_collisions (ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions (ai_settings, screen, ship, aliens, bullets):
    """ Responde a colisões entre projeteis e alienigenas"""        
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def check_fleet_edges(ai_settings, aliens):
    """Responde de maneira adeuqda quando algum alien atingir a borda"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens): 
    """ faz a frota descer e mudar de direcao"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, ship, aliens):
    """ Verifica se a frota está em uma das bordas e então atualiza as posições
de todos os alienígenas da frota."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update() 
    #verificar colisões entre alien e nave
    if pygame.sprite.spritecollideany(ship,aliens):
        print ('Nave atingida!')
    