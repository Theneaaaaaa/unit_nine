# Thenea Sun
# Dec. 20th
# A breakout game about letting ball hits the paddle and get points from it

import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball


def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW - 1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    color = [RED, ORANGE, YELLOW, GREEN, CYAN]
    mainSurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 32, 0)
    mainSurface.fill(WHITE)
    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)
    brick_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()
    brick_sound = pygame.mixer.Sound("brick_beep.wav")
    pygame.init()
    x = 0
    y = BRICK_Y_OFFSET
    for q in color:
        for z in range(2):
            for c in range(BRICKS_PER_ROW):
                my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, q)
                brick_group.add(my_brick)
                my_brick.rect.x = x
                my_brick.rect.y = y
                mainSurface.blit(my_brick.image, my_brick.rect)
                x = x + BRICK_WIDTH + BRICK_SEP
            y = y + BRICK_HEIGHT + BRICK_SEP
            x = 0

    paddle_1 = paddle.Paddle(mainSurface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_1.rect.x = APPLICATION_WIDTH / 2
    paddle_1.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    mainSurface.blit(paddle_1.image, paddle_1.rect)
    paddle_group.add(paddle_1)

    ball_1 = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    ball_1.rect.x = APPLICATION_HEIGHT / 2
    ball_1.rect.y = APPLICATION_WIDTH / 2
    mainSurface.blit(ball_1.image, ball_1.rect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        mainSurface.fill(WHITE)
        for x in brick_group:
            mainSurface.blit(x.image, x.rect)
        paddle_1.move()
        ball_1.move()
        ball_1.collide(paddle_group)
        ball_1.collideBrick(brick_group)
        mainSurface.blit(paddle_1.image, paddle_1.rect)
        mainSurface.blit(ball_1.image, ball_1.rect)

        if ball_1.collideBrick(brick_group):
            brick_sound.play()
            break

        if ball_1.rect.bottom >= APPLICATION_HEIGHT:
            ball_1.rect.x = APPLICATION_HEIGHT / 2
            ball_1.rect.y = APPLICATION_WIDTH / 2
            NUM_TURNS -= 1
        if NUM_TURNS == 0:
            print("Game Over")
            pygame.quit()
            sys.exit()
        else:
            print("You Won!")
        pygame.display.update()


main()
