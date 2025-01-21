import pygame

class Bin:
    def __init__(self, x, y, bin_type):
        self.x = x
        self.y = y
        self.bin_type = bin_type
        self.image = pygame.image.load(f'assets/images/{bin_type}_bin.png')
        self.image = pygame.transform.scale(self.image, (100, 100))  # Resize to 100x100 pixels

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))