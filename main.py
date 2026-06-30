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
graphic = draw.Draw(1000, 1000)
physic = physics.Physics()
m = mouse.Mouse()

# state = pi.getSetup()
# state = billiard.getSetup()
# state = rocket.getSetup()
state = jump.getSetup()
# state = onedCase.getSetup()
# state = sandBox.getSetup()

if state.counting:
    count = counter.Counter()

getTicksLastFrame = 0
running = True
paused = False
c = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break
        if event.type == pg.KEYDOWN and event.key == pg.K_p:
            paused = not paused
            continue
        m.handleEvent(event, state)
    m.tick()

    if not paused:
        c = physic.tick(state.objects, state.gravity, state.drag)

    if state.counting:
        count.countUp(c)
        graphic.paint(state.objects, count)
    else:
        graphic.paint(state.objects)

    clock.tick(1000)

pg.quit()