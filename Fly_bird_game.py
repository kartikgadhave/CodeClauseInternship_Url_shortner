import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BIRD_WIDTH, BIRD_HEIGHT = 50, 50
GRAVITY = 1
JUMP_HEIGHT = 15
PIPE_WIDTH, PIPE_HEIGHT = 80, 300
PIPE_SPEED = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Latest Bird Game")

# Load bird image
bird_image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT), pygame.SRCALPHA)
pygame.draw.circle(bird_image, BLUE, (BIRD_WIDTH // 2, BIRD_HEIGHT // 2), BIRD_WIDTH // 2)

# Create bird rect
bird_rect = bird_image.get_rect(center=(WIDTH // 4, HEIGHT // 2))

# Create pipes
pipes = []
pipe_spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_spawn_event, 2000)  # Trigger event every 2000 milliseconds

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
jumping = False
jump_count = 0
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                jump_count = JUMP_HEIGHT
        elif event.type == pipe_spawn_event:
            pipe_height = random.randint(50, HEIGHT - 200)
            pipes.append(pygame.Rect(WIDTH, 0, PIPE_WIDTH, pipe_height))
            pipes.append(pygame.Rect(WIDTH, pipe_height + 200, PIPE_WIDTH, HEIGHT - pipe_height - 200))

    # Bird jump
    if jumping:
        bird_rect.y -= jump_count
        jump_count -= 1
        if jump_count == 0:
            jumping = False

    # Bird gravity
    bird_rect.y += GRAVITY

    # Move pipes
    pipes = [pipe.move(-PIPE_SPEED, 0) for pipe in pipes]

    # Check for collisions with pipes
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            print("Game Over! Score:", score)
            running = False

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe.right > 0]

    # Check for scoring
    if pipes and bird_rect.x > pipes[0].x + PIPE_WIDTH:
        score += 1

    # Update display
    screen.fill(WHITE)

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

    # Draw bird
    screen.blit(bird_image, bird_rect)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
