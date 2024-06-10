import pygame
import numpy as np
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Snake:
    def __init__(self):
        self.position = [0, 0]
        self.direction = 'right'
        self.length = 1

    def update(self):
        # Mover la cabeza de la serpiente
        if self.direction == 'up':
            self.position[1] -= 1
        elif self.direction == 'down':
            self.position[1] += 1
        elif self.direction == 'left':
            self.position[0] -= 1
        elif self.direction == 'right':
            self.position[0] += 1

    #def draw(self, screen):
    #    # Dibujar la serpiente
    #    for i in range(self.length):
    #        pygame.draw.rect(screen, (255, 255, 255), (self.position[0] + i, self.position[1], 10, 10))
    
    def draw(self, screen):
        # Dibujar la cabeza de la serpiente
        head_color = (255, 255, 0)
        pygame.draw.rect(screen, head_color, (self.position[0], self.position[1], 10, 10))

        # Dibujar el cuerpo de la serpiente
        body_color = (255, 255, 255)
        for i in range(1, self.length):
            segment_position = (self.position[0] - i * 10, self.position[1])
            pygame.draw.rect(screen, body_color, segment_position, (10, 10))

    
    def grow(self):
        self.length += 10

class Food:
    def __init__(self):
        self.position = [np.random.randint(0, SCREEN_WIDTH), np.random.randint(0, SCREEN_HEIGHT)]

    def spawn(self):
        self.position = [np.random.randint(0, SCREEN_WIDTH), np.random.randint(0, SCREEN_HEIGHT)]

    def draw(self, screen):
        # Dibujar la comida
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0], self.position[1], 10, 10))
