import sys
import pygame


pygame.init()

# w gre gra się przy użyciu przycisków w i s oraz strzałek góra-dół

# settings
width = 800
height = 600
white = (255, 255, 255)
black = (0, 0, 0)
paddleWidth = 10
paddleHeight = 60
ballSize = 15
ballSpeedX = 3
ballSpeedY = 3
fps = 60

# screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping-Pong")

# paddles
leftPaddle = pygame.Rect(10, height/2-paddleHeight/2, paddleWidth, paddleHeight)
rightPaddle = pygame.Rect(width-20, height/2-paddleHeight/2, paddleWidth, paddleHeight)

# ball
ball = pygame.Rect(width/2-ballSize/2, height/2-ballSize/2, ballSize, ballSize)

# clock
clock = pygame.time.Clock()

# main game
playing = True
while playing:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    # key operations
    keys = pygame.key.get_pressed()

    # leftPaddle
    if keys[pygame.K_w] and leftPaddle.top > 0:
        leftPaddle.y -= 5
    if keys[pygame.K_s] and leftPaddle.bottom < height:
        leftPaddle.y += 5

    # rightPaddle
    if keys[pygame.K_UP] and rightPaddle.top > 0:
        rightPaddle.y -= 5
    if keys[pygame.K_DOWN] and rightPaddle.bottom < height:
        rightPaddle.y += 5

    # ball movement
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # collision with paddles
    if ball.colliderect(leftPaddle):
        ballSpeedX = abs(ballSpeedX)
        ball.x = leftPaddle.x + paddleWidth
    if ball.colliderect(rightPaddle):
        ballSpeedX = -abs(ballSpeedX)
        ball.x = rightPaddle.x - ballSize

    # collision with walls
    if ball.top <= 0 or ball.bottom >= height:
        ballSpeedY = -ballSpeedY

    # points
    if ball.left <= 0:
        print("Right player won!")
        ballSpeedX = abs(ballSpeedX)
        # reset positions
        ball.x = width / 2 - ballSize / 2
        ball.y = height / 2 - ballSize / 2
        leftPaddle.y = height / 2 - paddleHeight / 2
        rightPaddle.y = height / 2 - paddleWidth / 2

    if ball.right >= width:
        print("Left player won!")
        ballSpeedX = -abs(ballSpeedX)
        # reset positions
        ball.x = width / 2 - ballSize / 2
        ball.y = height / 2 - ballSize / 2
        leftPaddle.y = height / 2 - paddleWidth / 2
        rightPaddle.y = height / 2 - paddleHeight / 2

    # pygame.draw
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.rect(screen, white, leftPaddle)
    pygame.draw.rect(screen, white, rightPaddle)

    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
sys.exit()
