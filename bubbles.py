import pygame
import random

class Bubble:
    def __init__(self, x, y, item_type):
        self.x = x
        self.y = y
        self.item_type = item_type
        self.image = pygame.image.load(f'assets/images/{item_type}.png')
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize to 50x50 pixels
        self.speed = random.uniform(1, 3)
        self.direction = random.choice([-1, 1])  # Diagonal direction

    def update(self):
        self.y -= self.speed  # Move bubble up
        self.x += self.direction * self.speed / 2  # Move bubble diagonally

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))