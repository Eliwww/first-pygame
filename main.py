from pygame import *

class Player(sprite.Sprite):
    def __init__(self, p_image, x, y, size_x, size_y, speed_x, speed_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(p_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed_x = speed_x
        self.speed_y = speed_y

        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y 


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = Player('pacman.jpeg', 100, 350, 50, 50, 0, 0)


window = display.set_mode((700, 500))
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_w:
                player.speed_y = -5
            if e.key == K_s:
                player.speed_y = 5
            if e.key == K_a:
                player.speed_x = -5
            if e.key == K_d:
                player.speed_x = 5
        if e.type == KEYUP:
            if e.key == K_w:
                player.speed_y = 0
            if e.key == K_s:
                player.speed_y = 0
            if e.key == K_a:
                player.speed_x = 0
            if e.key == K_d:
                player.speed_x = 0

    window.fill((0, 0, 0))
    player.update()
    player.reset()
    time.delay(60)
    display.update()