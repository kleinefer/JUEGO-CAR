import pygame
import sys
import random

# Agrega una variable global para representar el nivel actual
nivel_actual = 1

# Define una función para aumentar el nivel
def aumentar_nivel():
    global nivel_actual
    if nivel_actual < 4:  # Limita el incremento hasta el nivel 3
        nivel_actual += 1

# Define una función para aumentar la velocidad y la dificultad según el nivel
def aumentar_dificultad(nivel):
    # Define la velocidad base y el incremento por nivel
    velocidad_base = 5
    incremento_por_nivel = 2  # Ajusta el incremento de velocidad según tu preferencia
    
    # Calcula la velocidad ajustada según el nivel
    velocidad = velocidad_base + (nivel - 1) * incremento_por_nivel
    
    # Incrementa la probabilidad de generación de obstáculos según el nivel
    probabilidad_base = 10
    incremento_probabilidad = 5  # Ajusta el incremento de probabilidad según tu preferencia
    probabilidad = probabilidad_base + (nivel - 1) * incremento_probabilidad
    
    return velocidad, probabilidad

def mostrar_nivel(PANTALLA, nivel):
    # Fuente para mostrar el nivel actual
    font_nivel = pygame.font.Font(None, 36)
    nivel_texto = font_nivel.render("Nivel " + str(nivel), True, (255, 255, 255))
    PANTALLA.blit(nivel_texto, (200, 10))

def start_carrera():
    global nivel_actual  # Importa la variable global nivel_actual

    # Inicializar Pygame
    pygame.init()

    # Configuración de la pantalla
    screen_width = 500
    screen_height = 600
    PANTALLA = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Juego de Carreras')

    # Colores
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)

    # Música de fondo
    pygame.mixer.music.load('sonido/compresssion_1.mp3')
    pygame.mixer.music.play(-1) # con -1 reproduce la música infinitamente
    pygame.mixer.music.set_volume(0.2) # Volumen

    # Cargar la imagen de fondo
    fondo = pygame.image.load("images/pistas.jpg")
    fondo = pygame.transform.scale(fondo, (screen_width, screen_height))

    # Cargar imágenes
    player_image = pygame.image.load('images/carroA.png')  # Ajusta la ruta según tu imagen
    player_image = pygame.transform.scale(player_image, (50, 100))

    obstacle_image = pygame.image.load('images/carroB.png')  # Ajusta la ruta según tu imagen
    obstacle_image = pygame.transform.scale(obstacle_image, (50, 100))

    # Jugador
    player_width = 50
    player_height = 50
    player_x = (screen_width - player_width) // 2
    player_y = screen_height - player_height - 50
    player_velocity, obstacle_probability = aumentar_dificultad(nivel_actual)

    # Obstáculos
    obstacle_width = 50
    obstacle_height = 50
    obstacles = []

    # Fuente para mostrar el puntaje y el Game Over
    font = pygame.font.Font(None, 36)

    # Reloj para controlar la velocidad de actualización
    clock = pygame.time.Clock()

    # Tiempo inicial (en milisegundos)
    start_time = pygame.time.get_ticks()

    # Variable para controlar el cambio de nivel
    cambio_nivel_aplicado = False

    # Ciclo principal del juego
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Actualizar el tiempo y el puntaje
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000
        score = int(elapsed_time)

        # Verificar si han pasado 60 segundos y aplicar el aumento de nivel
        if score >= 10 and not cambio_nivel_aplicado:
            aumentar_nivel()  # Aumenta el nivel
            player_velocity, obstacle_probability = aumentar_dificultad(nivel_actual)  # Actualiza la velocidad y la probabilidad
            cambio_nivel_aplicado = True  # Marca el cambio de nivel como aplicado

        # Movimiento del jugador
        if keys[pygame.K_LEFT] and player_x - player_velocity > 0:
            player_x -= player_velocity
        if keys[pygame.K_RIGHT] and player_x + player_velocity < screen_width - player_width:
            player_x += player_velocity

        # Generar obstáculos
        if random.randint(1, 600) < obstacle_probability:  # Probabilidad de generar un obstáculo
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            obstacle_y = -obstacle_height
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        # Mover obstáculos
        for obstacle in obstacles:
            obstacle.y += player_velocity
            if obstacle.y > screen_height:
                obstacles.remove(obstacle)

        # Colisión con obstáculos
        for obstacle in obstacles:
            if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(obstacle):
                running = False

        # Limpiar la pantalla
        PANTALLA.blit(fondo, (0, 0))

        # Dibujar al jugador y los obstáculos
        PANTALLA.blit(player_image, (player_x, player_y))
        for obstacle in obstacles:
            PANTALLA.blit(obstacle_image, obstacle)

        # Mostrar el puntaje y el nivel
        score_text = font.render("Puntaje: " + str(score), True, BLANCO)
        PANTALLA.blit(score_text, (10, 10))
        mostrar_nivel(PANTALLA, nivel_actual)

        # Si el juego ha terminado, mostrar "Game Over"
        if not running:
            game_over_text = font.render("Game Over", True, ROJO)
            PANTALLA.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2))

        # Actualizar la pantalla
        pygame.display.update()
        clock.tick(60)

    # No es necesario salir del juego aquí
    # pygame.quit()
    # sys.exit()

if __name__ == "__main__":
    start_carrera()
