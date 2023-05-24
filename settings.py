

class Settings():
    """Aqui iremos armazenar todas as configuracoes do jogo """

    def __init__(self):
        #Config da tela
        self.screen_width = 900
        self.screen_height = 1100
        self.bg_color = (255,255,255)

        #configurações da nave 
        self.ship_speed_factor = 3  #Velocidade da Nave
        self.ship_limit = 3 #quantidade de naves 
        
        #Configuração dos tiros
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = 255, 0, 255
        self.bullets_allowed = 20
       
        #alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20  

        #fleet = 1 -> significa direita e -1 significa esquerda
        self.fleet_direction = 1