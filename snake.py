import pygame
import random
 
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
 
# snake starting position (each part is [x, y])
snake = [[100, 100], [80, 100], [60, 100]]
 
# direction: moving right at the start
dx = 20
dy = 0
 
# direction chosen by key (used on the next move)
next_dx = 20
next_dy = 0
 
food = [300, 200]
score = 0
running = True
 
while running:
    # keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                next_dx = 0
                next_dy = -20
            if event.key == pygame.K_DOWN and dy == 0:
                next_dx = 0
                next_dy = 20
            if event.key == pygame.K_LEFT and dx == 0:
                next_dx = -20
                next_dy = 0
            if event.key == pygame.K_RIGHT and dx == 0:
                next_dx = 20
                next_dy = 0
 
    # use the chosen direction (only once per move)
    dx = next_dx
    dy = next_dy
 
    # move snake: add new head
    head_x = snake[0][0] + dx
    head_y = snake[0][1] + dy
    snake.insert(0, [head_x, head_y])
 
    # check food
    if head_x == food[0] and head_y == food[1]:
        score = score + 1
        food = [random.randint(0, 29) * 20, random.randint(0, 19) * 20]
    else:
        snake.pop()  # remove tail if no food eaten
 
    # hit wall
    if head_x < 0 or head_x >= 600 or head_y < 0 or head_y >= 400:
        running = False
 
    # hit itself
    if [head_x, head_y] in snake[1:]:
        running = False
 
    # draw
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 20, 20))
    for part in snake:
        pygame.draw.rect(screen, (0, 255, 0), (part[0], part[1], 20, 20))
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
 
    pygame.display.flip()
    clock.tick(10)
 
pygame.quit()
 
