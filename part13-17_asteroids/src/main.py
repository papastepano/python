# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10
        elif event.type == pygame.QUIT:
            exit()

    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()