import pygame as pg
import draw
import physics
import counter
import setups.pi as pi
import setups.billiard as billiard
import setups.rocket as rocket
import setups.onedCase as onedCase

pg.init()
clock = pg.time.Clock()
graphic = draw.Draw(1000, 1000)
physic = physics.Physics()

# state = pi.getSetup()
# state = billiard.getSetup()
# state = rocket.getSetup()
state = onedCase.getSetup()

if state.counting:
    count = counter.Counter()

getTicksLastFrame = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    c = physic.tick(state.objects, state.gravity, state.drag)

    if state.counting:
        count.countUp(c)
        graphic.paint(state.objects, count)
    else:
        graphic.paint(state.objects)

    clock.tick(1000)

pg.quit()