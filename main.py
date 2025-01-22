import pygame
import random
from bubbles import Bubble
from utils import increase_difficulty

def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main_menu(screen, font):
    menu = True
    while menu:
        screen.fill((255, 255, 255))
        draw_text(screen, "Bubble Recycler", font, (0, 0, 0), 300, 100)
        draw_text(screen, "1. Start Game", font, (0, 0, 0), 300, 200)
        draw_text(screen, "2. Instructions", font, (0, 0, 0), 300, 300)
        draw_text(screen, "3. Quit", font, (0, 0, 0), 300, 400)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "start"
                elif event.key == pygame.K_2:
                    return "instructions"
                elif event.key == pygame.K_3:
                    pygame.quit()
                    exit()

def instructions_menu(screen, font):
    instructions = True
    while instructions:
        screen.fill((255, 255, 255))
        draw_text(screen, "Instructions", font, (0, 0, 0), 300, 100)
        draw_text(screen, "Slice the plastic items to score points.", font, (0, 0, 0), 100, 200)
        draw_text(screen, "Avoid slicing the general waste items (bombs).", font, (0, 0, 0), 100, 250)
        draw_text(screen, "Press any key to return to the main menu.", font, (0, 0, 0), 100, 400)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                return

def game_loop(screen, font):
    clock = pygame.time.Clock()
    bubbles = []
    item_types = ['plastic', 'paper', 'can', 'food_scraps', 'wrappers', 'hazardous_materials']
    score = 0
    level = 1
    spawn_interval = 20

    pop_sound = pygame.mixer.Sound('Assets/Sounds/pop.mp3')
    slice_sound = pygame.mixer.Sound('Assets/Sounds/slice.wav')
    background_music = pygame.mixer.music.load('Assets/Sounds/background.mp3')
    pygame.mixer.music.play(-1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for bubble in bubbles[:]:
                    if bubble.x <= mouse_x <= bubble.x + 60 and bubble.y <= mouse_y <= bubble.y + 60:
                        bubble.pop()
                        pop_sound.play()
                        bubbles.remove(bubble)  # Remove the bubble after popping
                        if bubble.item_type in ['food_scraps', 'wrappers', 'hazardous_materials']:
                            running = False  # End game if a bomb is popped
                        else:
                            score += 10
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                for bubble in bubbles[:]:
                    if bubble.x <= mouse_x <= bubble.x + 60 and bubble.y <= mouse_y <= bubble.y + 60:
                        bubble.slice()
                        slice_sound.play()
                        bubbles.remove(bubble)  # Remove the bubble after slicing
                        if bubble.item_type in ['food_scraps', 'wrappers', 'hazardous_materials']:
                            running = False  # End game if a bomb is sliced
                        else:
                            score += 10

        # Spawn bubbles randomly
        if random.randint(1, spawn_interval) == 1:
            x = random.randint(0, 740)  # Spawn within screen width
            y = random.randint(0, 100)  # Limit spawn area to the top 100 pixels
            item_type = random.choice(item_types)
            bubbles.append(Bubble(x, y, item_type))

        # Update bubbles
        for bubble in bubbles[:]:
            if bubble.update():
                bubbles.remove(bubble)

        # Increase difficulty
        if pygame.time.get_ticks() % 60000 == 0:  # Every 60 seconds
            level += 1
            spawn_interval = max(1, spawn_interval - 1)

        # Draw everything
        screen.fill((255, 255, 255))
        for bubble in bubbles:
            bubble.draw(screen)

        # Draw scoreboard
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    return score

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bubble Recycler")
    font = pygame.font.Font(None, 36)  # Font for the scoreboard

    while True:
        choice = main_menu(screen, font)
        if choice == "start":
            score = game_loop(screen, font)
            print(f"Game Over! Your score: {score}")
        elif choice == "instructions":
            instructions_menu(screen, font)

if __name__ == "__main__":
    main()