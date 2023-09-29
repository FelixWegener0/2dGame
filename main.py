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

# value for player speed
movingValue = 20

# coordinates relative to the screen
relative_x = 0
relative_y = 0

# value to check if player can access in direction
allowMoveLeft = True
allowMoveRight = True
allowMoveUp = True
allowMoveDown = True

# global variable for first oject
object_x1 = 0
movingToLeft1 = True

# global variable for second object
object_x2 = 0
movingToLeft2 = True

# check if the player gets near object in x dimension
def checkHitX(playerX, objectX, threshhold=60):
    spaceBetween = playerX - objectX
    if -threshhold <= spaceBetween <= threshhold:
        return True 

# check if the player gets near object in y dimension
def checkHitY(playerY, objectY, threshhold=60):
    spaceBetween = playerY - objectY
    if -threshhold <= spaceBetween <= threshhold:
        return True

# handle update the objects position on screen
def handleUpdateMovingObjectPosition(this_object_x, movingToLeftCase, moveValue=10):
        local_movingLeft = movingToLeftCase

        if this_object_x > -1 and this_object_x < screen.get_width() and local_movingLeft:
            return this_object_x + moveValue

        if this_object_x >= screen.get_width():
            local_movingLeft = False

        if this_object_x > -1 and local_movingLeft == False:
            return this_object_x - moveValue

        if this_object_x < 1:
            local_movingLeft = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # draw player
    circlePosition = pygame.Vector2(relative_x + screen.get_width() / 2, relative_y + screen.get_height())
    pygame.draw.circle(screen, "red", circlePosition, 40)

    # handle first moving object
    pygame.draw.circle(screen, "black", pygame.Vector2( object_x1, screen.get_height() / 2) ,40)

    object_x1 = handleUpdateMovingObjectPosition(object_x1, movingToLeft1)
    if object_x1 > screen.get_width() - 10:
        movingToLeft1 = False
    if object_x1 < 10:
        movingToLeft1 = True

    if checkHitX(relative_x + screen.get_width() / 2, object_x1) and checkHitY(relative_y + screen.get_height(), screen.get_height() / 2):
        running = False

    # handel second moving object
    pygame.draw.circle(screen, "black", pygame.Vector2( object_x2, screen.get_height() / 2 + 100) ,40)
    object_x2 = handleUpdateMovingObjectPosition(object_x2, movingToLeft2, 25)

    if object_x2 > screen.get_width() - 10:
        movingToLeft2 = False
    if object_x2 < 10:
        movingToLeft2 = True

    if checkHitX(relative_x + screen.get_width() / 2, object_x2) and checkHitY(relative_y + screen.get_height(), screen.get_height() / 2 + 100):
        running = False


    # enable player to move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and allowMoveUp:
        relative_y -= movingValue
    if keys[pygame.K_s] and allowMoveDown:
        relative_y += movingValue
    if keys[pygame.K_a] and allowMoveLeft:
        relative_x -= movingValue
    if keys[pygame.K_d] and allowMoveRight:
        relative_x += movingValue

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
