import pygame
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


pygame.init()

WIDTH = 600
HEIGHT = 600
SQUARE_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
line = pygame.draw.line(screen,(0,0,0),(0,0),(600,0),79)
snake_pos = [(WIDTH // 2, HEIGHT // 2), (WIDTH // 2, HEIGHT // 2 + SQUARE_SIZE), (WIDTH // 2, HEIGHT // 2 + 2 * SQUARE_SIZE)]
snake_dir = (0, -20)  #
food_pos = (random.randint(0, WIDTH // 20 - 1) * 20, random.randint(0, HEIGHT // 20 - 1) * 20)
score = 0
font = pygame.font.Font(None, 36)
high_score = [0,440]
clock = pygame.time.Clock()
running = True
game_started = False
game_over = False
def buncha_boxes():
    for x in range(0, WIDTH, 20):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT), 2)
    for y in range(0, HEIGHT, 20):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y), 2)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_started:
            if event.key == pygame.K_SPACE:
                game_started = True
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                game_started = False
                game_over = False
                snake_pos = [(WIDTH // 2, HEIGHT // 2), (WIDTH // 2, HEIGHT // 2 + SQUARE_SIZE),
                             (WIDTH // 2, HEIGHT // 2 + 2 * SQUARE_SIZE)]
                snake_dir = (0, -20)
                food_pos = (random.randint(0, WIDTH // 20 - 1) * 20, random.randint(0, HEIGHT // 20 - 1) * 20)
                score = 0

    if not game_started:
        screen.fill(WHITE)
        start_text = font.render("Press SPACE to Start", True, BLACK)
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - start_text.get_height() // 2))
        pygame.display.flip()
        continue

    if game_over:
        screen.fill(WHITE)
        game_over_text = font.render("Game Over", True, BLACK)
        restart_text = font.render("Press R to Restart", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + game_over_text.get_height() // 2))
        pygame.display.flip()
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_dir != (20, 0):
        snake_dir = (-20, 0)
    elif keys[pygame.K_RIGHT] and snake_dir != (-20, 0):  
        snake_dir = (20, 0)
    elif keys[pygame.K_UP] and snake_dir != (0, 20):
        snake_dir = (0, -20)
    elif keys[pygame.K_DOWN] and snake_dir != (0, -20): 
        snake_dir = (0, 20)
    elif keys[pygame.K_a] and snake_dir != (20, 0):
        snake_dir = (-20, 0)
    elif keys[pygame.K_d] and snake_dir != (-20, 0):  
        snake_dir = (20, 0)
    elif keys[pygame.K_w] and snake_dir != (0, 20):
        snake_dir = (0, -20)
    elif keys[pygame.K_s] and snake_dir != (0, -20): 
        snake_dir = (0, 20)

    new_head = (snake_pos[0][0] + snake_dir[0], snake_pos[0][1] + snake_dir[1])
    if new_head in snake_pos or new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or pygame.Rect(new_head, (20, 20)).colliderect(line):
        game_over = True
        high_score.append(score)
        high_score.sort(reverse = True)
    snake_pos.insert(0, new_head)
    if new_head == food_pos:
        food_pos = (random.randint(0, WIDTH // 20 - 1) * 20, random.randint(0, HEIGHT // 20 - 1) * 20)
        score += 10
    elif food_pos in snake_pos or food_pos[1] < 40:
        food_pos = (random.randint(0, WIDTH // 20 - 1) * 20, random.randint(0, HEIGHT // 20 - 1) * 20)
    else:
        snake_pos.pop()

    screen.fill((WHITE))
    for pos in snake_pos:
        pygame.draw.rect(screen, (0, 125, 0), pygame.Rect(pos[0], pos[1], 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 20, 20))
    pygame.draw.line(screen,BLACK,(0,0),(600,0),80)
    buncha_boxes()
    high_score_text = font.render(f"High Score: {str(high_score[0])}", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text ,(300, 10))
    
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
