import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Rivals")

clock = pygame.time.Clock()

# Player settings
player1 = pygame.Rect(100, 300, 50, 50)
player2 = pygame.Rect(650, 300, 50, 50)

speed = 5

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 80, 80)
BLACK = (20, 20, 20)

def draw():
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, BLUE, player1)
    pygame.draw.rect(screen, RED, player2)
    
    pygame.display.update()

def handle_movement(keys):
    # Player 1 (WASD)
    if keys[pygame.K_a]:
        player1.x -= speed
    if keys[pygame.K_d]:
        player1.x += speed
    if keys[pygame.K_w]:
        player1.y -= speed
    if keys[pygame.K_s]:
        player1.y += speed

    # Player 2 (Arrow keys)
    if keys[pygame.K_LEFT]:
        player2.x -= speed
    if keys[pygame.K_RIGHT]:
        player2.x += speed
    if keys[pygame.K_UP]:
        player2.y -= speed
    if keys[pygame.K_DOWN]:
        player2.y += speed

def main():
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        handle_movement(keys)
        draw()

if __name__ == "__main__":
    main()
