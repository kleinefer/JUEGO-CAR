import pygame
import sys

class GameNavigation:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.PANTALLA = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Juego de Arcade')
        self.NEGRO = (0, 0, 0)
        self.BLANCO = (255, 255, 255)
        self.fondo = pygame.image.load("images/pistamenu.jpg")
        self.fondo = pygame.transform.scale(self.fondo, (800, 600))

    def start_instrucciones(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:  # Detecta la tecla de retroceso
                        return  # Volver al menú principal

            keys = pygame.key.get_pressed()
            self.display_instructions()
            pygame.display.update()

        pygame.quit()
        sys.exit()

    def display_instructions(self):
        font = pygame.font.Font(None, 36)
        instruction_text1 = font.render("¡INTRUCIONES!", True, self.BLANCO)
        instruction_text2 = font.render("Mueve el auto usando las flechas izq y der.", True, self.BLANCO)
        instruction_text3 = font.render("Evita que los autos rojos te choquen ", True, self.BLANCO)
        instruction_text4 = font.render("ve sumando puntaje con el tiempo transcurrido.", True, self.BLANCO)
        #instruction_text5 = font.render("Presiona la tecla de retroceso para volver al menú principal.", True, self.BLANCO)

        # Dibuja el fondo
        self.PANTALLA.blit(self.fondo, (0, 0))
        self.PANTALLA.blit(instruction_text1, (150, 200))
        self.PANTALLA.blit(instruction_text2, (120, 250))
        self.PANTALLA.blit(instruction_text3, (120, 300))
        self.PANTALLA.blit(instruction_text4, (120, 350))
       # self.PANTALLA.blit(instruction_text5, (120, 450))

       
        pygame.display.update()
