import pygame
import random
from bubbles import Bubble
from bins import Bin
from utils import calculate_score, increase_difficulty

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bubble Recycler")
    clock = pygame.time.Clock()

    bubbles = []
    item_types = ['plastic', 'paper', 'can', 'food_scraps', 'wrappers', 'hazardous_materials']
    score = 0
    level = 1
    spawn_interval = 20

    recycling_bin = Bin(350, 500, 'recycling')
    general_bin = Bin(450, 500, 'general')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for bubble in bubbles[:]:
                    if bubble.x <= mouse_x <= bubble.x + 50 and bubble.y <= mouse_y <= bubble.y + 50:
                        bubbles.remove(bubble)
                        score += calculate_score(bubble.item_type, 'general')
                        # Add sound effect for popping

        # Spawn bubbles randomly
        if random.randint(1, spawn_interval) == 1:
            x = random.choice([0, 800])
            y = random.randint(0, 600)
            item_type = random.choice(item_types)
            bubbles.append(Bubble(x, y, item_type))

        # Update bubbles
        for bubble in bubbles:
            bubble.update()
            if bubble.y < 0:
                bubbles.remove(bubble)
                score += calculate_score(bubble.item_type, 'recycling')
                # Add sound effect for recycling

        # Increase difficulty
        if pygame.time.get_ticks() % 60000 == 0:  # Every 60 seconds
            level += 1
            spawn_interval = max(1, spawn_interval - 1)

        # Draw everything
        screen.fill((255, 255, 255))
        recycling_bin.draw(screen)
        general_bin.draw(screen)
        for bubble in bubbles:
            bubble.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()