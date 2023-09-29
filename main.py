import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# player position in screen center
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_color = "red"

# coordinates relative to the screen
relative_x = 0
relative_y = 0

# value to move the screen to simulate player move
moveValue = 10

# value to check if player can access in direction
allowMoveLeft = True
allowMoveRight = True
allowMoveUp = True
allowMoveDown = True

x = 0
movingToLeft = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # pygame.draw.circle(screen, player_color, player_pos, 40)

    # circlePosition = pygame.Vector2(relative_x + 0, relative_y + 0)
    # pygame.draw.circle(screen, "black", circlePosition, 40)

    # lineVector1 = pygame.Vector2(relative_x + 0, relative_y + 2)
    # lineVector2 = pygame.Vector2( relative_x + 0, relative_y + 1000)

    # pygame.draw.line(screen, "black", lineVector1, lineVector2, 40)
    vector = pygame.Vector2( x, screen.get_height() / 2)

    pygame.draw.circle(screen, "black", vector ,40)
    
    # handle moving side to side
    if x > -1 and x < screen.get_width() and movingToLeft:
        x = x + moveValue
    if x >= screen.get_width():
        movingToLeft = False
    if x > -1 and movingToLeft == False:
        x = x - moveValue
    if x < 1:
        movingToLeft = True

    # print(lineVector1.distance_to(player_pos))
    # print(lineVector1.distance_squared_to(player_pos))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and allowMoveUp:
        relative_y += moveValue
    if keys[pygame.K_s] and allowMoveDown:
        relative_y -= moveValue
    if keys[pygame.K_a] and allowMoveLeft:
        relative_x += moveValue
    if keys[pygame.K_d] and allowMoveRight:
        relative_x -= moveValue

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
