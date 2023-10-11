import pygame

class Player:
    def __init__(self, x=0, y=0, name='default', color='red', radius=20):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
        self.radius = radius
        
        self.allowMovingUp = True
        self.allowMovingDown = True
        self.allowMovingLeft = True
        self.allowMovingRight = True


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, pygame.Vector2(self.x, self.y), self.radius)

    def move(self, screen, speed=20):
        keys = pygame.key.get_pressed()

        if (self.x <= 10): self.allowMovingLeft = False
        else: self.allowMovingLeft = True

        if (self.x >= screen.get_width()): self.allowMovingRight = False
        else: self.allowMovingRight = True

        if (self.y <= 10): self.allowMovingUp = False
        else: self.allowMovingUp = True

        if (self.y >= screen.get_height()): self.allowMovingDown = False
        else: self.allowMovingDown = True


        if (keys[pygame.K_w] and self.allowMovingUp): self.y = self.y - speed
        if (keys[pygame.K_s] and self.allowMovingDown): self.y = self.y + speed
        if (keys[pygame.K_a] and self.allowMovingLeft): self.x = self.x - speed
        if (keys[pygame.K_d] and self.allowMovingRight): self.x = self.x + speed

    def getPlayerX(self):
        return self.x
    
    def getPlayerY(self):
        return self.y