import pygame
import enemy as en
import player as pl

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player1 = pl.Player(screen.get_width() / 2, screen.get_height())

enemys = []
for i in range(8):
    enemys.append(en.Enemy(0, screen.get_height() / 2  - i * 40))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("gray")

    player1.draw(screen)
    player1.move(screen)

    for i in range(len(enemys)):
        enemys[i].draw(screen)
        enemys[i].moveEnemy(screen, 5 * i + 10)
        if (enemys[i].hitPlayer(player1.x, player1.y)): running = False

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
