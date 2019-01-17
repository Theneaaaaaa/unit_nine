import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()
        # finish setting the class variables to the parameters
        self.color = color
        self.radius = radius
        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.Surface((self.radius, self.radius))
        self.rect = self.image.get_rect()
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        # Add a circle to represent the ball to the surface just created.
        self.speed_x = 7
        self.speed_y = 6
        self.brick_sound = pygame.mixer.Sound("beep.wav")
        self.paddle_sound = pygame.mixer.Sound("paddle.wav")

    def move(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        if self.rect.right >= self.windowWidth:
            self.speed_x = -self.speed_x
        elif self.rect.left <= 0:
            self.speed_x = -self.speed_x
        elif self.rect.top <= 0:
            self.speed_y = -self.speed_y
            self.speed_x = self.speed_x

    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.speed_y = -self.speed_y
            self.paddle_sound.play()

    def collideBrick(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.speed_y = -self.speed_y
            self.brick_sound.play()
