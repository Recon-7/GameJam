import pygame

class Bin:
    def __init__(self, x, y, bin_type):
        self.x = x
        self.y = y
        self.bin_type = bin_type

    def draw(self, screen):
        if self.bin_type == 'recycling':
            color = (0, 128, 0)  # Green for recycling bin
        else:
            color = (128, 128, 128)  # Gray for general bin
        pygame.draw.rect(screen, color, (self.x, self.y, 100, 100))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 100, 100), 2)  # Black border

    def collides_with(self, item_x, item_y):
        return self.x <= item_x <= self.x + 100 and self.y <= item_y <= self.y + 100