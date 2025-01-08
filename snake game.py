import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

def main():
    # Initialize snake and food
    snake = [(100, 100)]
    snake_dir = "RIGHT"
    food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
            random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)
    score = 0

    def draw_snake(snake):
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, BLOCK_SIZE, BLOCK_SIZE))

    def move_snake(snake, direction):
        x, y = snake[0]
        if direction == "UP":
            y -= BLOCK_SIZE
        elif direction == "DOWN":
            y += BLOCK_SIZE
        elif direction == "LEFT":
            x -= BLOCK_SIZE
        elif direction == "RIGHT":
            x += BLOCK_SIZE
        new_head = (x, y)
        snake = [new_head] + snake[:-1]
        return snake

    def check_collision(snake):
        # Check if the snake collides with itself or the boundaries
        head = snake[0]
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True
        if head in snake[1:]:
            return True
        return False

    running = True
    global food
    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir != "DOWN":
                    snake_dir = "UP"
                elif event.key == pygame.K_DOWN and snake_dir != "UP":
                    snake_dir = "DOWN"
                elif event.key == pygame.K_LEFT and snake_dir != "RIGHT":
                    snake_dir = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_dir != "LEFT":
                    snake_dir = "RIGHT"

        # Move the snake
        snake = move_snake(snake, snake_dir)

        # Check if the snake eats food
        if snake[0] == food:
            snake.append(snake[-1])  # Grow the snake
            food = (random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                    random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)
            score += 1

        # Check for collisions
        if check_collision(snake):
            print(f"Game Over! Your Score: {score}")
            running = False

        # Draw snake and food
        draw_snake(snake)
        pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))

        # Update display
        pygame.display.flip()

        # Control frame rate
        clock.tick(10)

    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main()
