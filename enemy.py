import pygame

class Enemy:
    def __init__(self, relative_x=0, relative_y=0, direction='RIGHT', radius=20):
        self.x = relative_x
        self.y = relative_y
        self.radius = radius
        self.direction = direction

    def draw(self, screen):
        pygame.draw.circle(screen, "black", pygame.Vector2(self.x, self.y), self.radius)

    def moveEnemy(self, screen, speed=10):
        if (self.x <= 10 and self.direction == 'LEFT'): self.direction = 'RIGHT'
        if (self.x >= screen.get_width() and self.direction == 'RIGHT'): self.direction = 'LEFT'

        if (self.direction == 'RIGHT'): self.x = self.x + speed
        if (self.direction == 'LEFT'): self.x = self.x - speed
            

    def hitPlayer(self, playerX, playerY, threshold=40):
        xSpace = playerX - self.x
        ySpace = playerY - self.y

        if (-threshold <= xSpace <= threshold and -threshold <= ySpace <= threshold) : return True
        return False

