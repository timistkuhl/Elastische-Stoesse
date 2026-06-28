import pygame as pg
import draw
import physics
import counter
import setups.pi as pi
import setups.billiard as billiard
import setups.rocket as rocket
import setups.onedCase as onedCase
import setups.sandBox as sandBox
import setups.jumpingballs as jump
import mouse

pg.init()
clock = pg.time.Clock()
graphic = draw.Draw(800, 600)
physic = physics.Physics()
m = mouse.Mouse()

# state = pi.getSetup()
# state = billiard.getSetup()
# state = rocket.getSetup()
state = jump.getSetup()

if state.counting:
    count = counter.Counter()

getTicksLastFrame = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break
        m.handleEvent(event, state)
    m.tick()

    c = physic.tick(state.objects, state.gravity, state.drag)

    if state.counting:
        count.countUp(c)
        graphic.paint(state.objects, count)
    else:
        graphic.paint(state.objects)

    clock.tick(1000)

pg.quit()