import pygame
from sprites import Snake, Food

# Configuración
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Inicialización
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Objetos
snake = Snake()
food = Food()

# Bucle principal
running = True
while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Controles de la serpiente
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = 'up'
            elif event.key == pygame.K_DOWN:
                snake.direction = 'down'
            elif event.key == pygame.K_LEFT:
                snake.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                snake.direction = 'right'

    # Actualización
    snake.update()

    # Comprobación de colisiones
    if snake.position == food.position:
        # La serpiente come la comida
        snake.grow()
        food.spawn()

    # Renderizado
    screen.fill((0, 0, 0))
    snake.draw(screen)
    food.draw(screen)

    # Actualización de la pantalla
    pygame.display.update()

    # Limitación de FPS
    clock.tick(FPS)

# Finalización
pygame.quit()
