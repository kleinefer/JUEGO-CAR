import pygame
import sys
from Carrera import start_carrera
from instrucciones import GameNavigation

pygame.init()

# Configuración de la pantalla
ancho, alto = 800, 600
PANTALLA = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Menú")

# Cargar la imagen de fondo
fondo = pygame.image.load("images/pistamenu.jpg")
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Colores
BLANCO = (255, 255, 255)

# Fuente
font = pygame.font.Font(None, 36)

# Opciones del menú
menu_options = ["Jugar", "Instrucciones", "Salir"]

# Variable de estado para controlar si el juego está en curso
juego_en_curso = False

# Función para mostrar el menú
def show_menu():
    global juego_en_curso
    navigation = GameNavigation()  # Crea una instancia de la clase GameNavigation
    while not juego_en_curso:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, option in enumerate(menu_options):
                    text = font.render(option, True, BLANCO)
                    text_rect = text.get_rect(center=(ancho // 2, alto // 2 - len(menu_options) * text.get_height() // 2 + i * 50))
                    if text_rect.collidepoint(mouse_pos):
                        if i == 0:  # Juego Carreras
                            start_carrera()
                            juego_en_curso = True
                            return  # Salir de la función después de iniciar el juego
                        elif i == 1:  # Instrucciones
                            retorno = navigation.start_instrucciones()  # Llama al método start_instrucciones de GameNavigation
                            if retorno == 'menu':  # Si se devuelve 'menu', vuelve al menú principal
                                return
                        elif i == 2:  # Salir
                            pygame.quit()
                            sys.exit()

        # Dibuja el fondo
        PANTALLA.blit(fondo, (0, 0))

        # Dibuja las opciones del menú
        for i, option in enumerate(menu_options):
            text = font.render(option, True, BLANCO)
            text_rect = text.get_rect(center=(ancho // 2, alto // 2 - len(menu_options) * text.get_height() // 2 + i * 50))
            PANTALLA.blit(text, text_rect)

        pygame.display.flip()

# Llama a la función para mostrar el menú
show_menu()
