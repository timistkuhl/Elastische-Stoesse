import pygame

class Draw:
    def __init__(self, height, width):
        screen = pygame.display.set_mode((height, width))
        pygame.display.set_caption("Elastische Stoesse")

# # genutzte Farbe
ORANGE  = ( 255, 140, 0)
# ROT     = ( 255, 0, 0)
# GRUEN   = ( 0, 255, 0)
# SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

def paintBalls(balls):
    screen.fill(WEISS)
    for ball in balls:
        pygame.draw.circle(screen, ORANGE, ball.position, ball.radius)

# Bildschirm Aktualisierungen einstellen
def quitGraphic():
    pygame.quit()

t = 0
spielaktiv = True
# Schleife Hauptprogramm
while spielaktiv:




    # Spiellogik hier integrieren
    # Spielfeld löschen


    # Spielfeld/figuren zeichnen

    pygame.draw.circle(screen, ORANGE, [250+1*t, 250-0.01*t**3], 1)

    pygame.draw.circle(screen, ROT, [200+1*t, 300-t*1], 1)
    # Fenster aktualisieren
    pygame.display.flip()
    t+=1
    # Refresh-Zeiten festlegen
    clock.tick(60)

# def main():
#     ball1 = new 

