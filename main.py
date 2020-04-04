import pygame as pg

pg.init()

screen = pg.display.set_mode((800, 600))

pg.display.set_caption('Space Invaders')
icon = pg.image.load('images/icon.png')
pg.display.set_icon(icon)


spaceship = pg.image.load('images/spaceship.png')
spaceshipX = 400
spaceshipY = 500


velocity = 0.6
spaceship_change = 0

def player(x, y):
    screen.blit(spaceship, (x, y))

running = True
while running:
    screen.fill((255,255,255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                spaceship_change = -velocity
            if event.key == pg.K_RIGHT:
                spaceship_change = velocity

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                spaceship_change = 0

    spaceshipX += spaceship_change

    if spaceshipX <= 0:
        spaceship = 0
    elif spaceshipX >= 736:
        spaceshipX = 736


    player(spaceshipX, spaceshipY)
    pg.display.update()
