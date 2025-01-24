import pygame
import random

class Bubble:
    def __init__(self, x, y, item_type):
        self.x = x
        self.y = y
        self.item_type = item_type
        self.image = pygame.image.load(f'Assets/Images/{item_type}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))  # Resize to 60x60 pixels
        self.speed = random.uniform(0.5, 1)  # Slower speed
        self.direction = random.choice([-1, 1])  # Horizontal direction
        self.popped = False
        self.current_frame = 0
        self.sliced = False
        self.velocity_y = random.uniform(-5, -7.5)  # Slower initial upward velocity
        self.gravity = 0.25  # Reduced gravity effect

        # Set color based on item type
        if item_type in ['food_scraps', 'wrappers', 'hazardous_materials']:
            self.color = (255, 0, 0)  # Red for general waste
        else:
            self.color = (0, 255, 0)  # Green for recyclable items

    def update(self):
        if not self.popped and not self.sliced:
            self.x += self.direction * self.speed  # Move bubble horizontally
            self.y += self.velocity_y  # Apply vertical velocity
            self.velocity_y += self.gravity  # Apply gravity
        elif self.popped:
            self.current_frame += 1
            if self.current_frame >= 10:  # Animation lasts for 10 frames
                self.popped = False  # Reset popped state
        return self.y > 600  # Return True if the item falls out of the screen

    def draw(self, screen):
        if not self.popped and not self.sliced:
            # Draw bubble
            pygame.draw.circle(screen, (*self.color, 128), (self.x + 30, self.y + 30), 35)  # Color with transparency
            pygame.draw.circle(screen, self.color, (self.x + 30, self.y + 30), 35, 2)  # Outline
            screen.blit(self.image, (self.x, self.y))  # Draw item inside bubble
        elif self.sliced:
            screen.blit(self.image, (self.x, self.y))  # Draw sliced item
        else:
            # Create a simple pop animation by scaling down the bubble
            scale = max(70 - self.current_frame * 7, 0)  # Reduce size each frame
            if scale > 0:
                pygame.draw.circle(screen, (*self.color, 128), (self.x + 30, self.y + 30), scale // 2)  # Color with transparency
                pygame.draw.circle(screen, self.color, (self.x + 30, self.y + 30), scale // 2, 2)  # Outline

    def pop(self):
        self.popped = True
        self.current_frame = 0

    def slice(self):
        self.sliced = True