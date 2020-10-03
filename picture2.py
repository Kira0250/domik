import pygame
import math
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 400))
Dom = pygame.Surface((1000, 400))
Dom.set_colorkey((0,0,0))
rect(screen, (0, 255, 0), (10, 210, 1000, 200))
rect(screen, (0, 0, 180), (10, 10, 1000, 200))

rect(Dom, (255, 0, 255), (100, 100, 200, 200))
rect(Dom, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(Dom, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
polygon(Dom, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)

rect(Dom, (255, 255, 255), (150, 150, 90, 50))
rect(Dom, (0, 0, 255), (150, 150, 90, 50), 5)



circle(Dom, (255, 255, 255), (350, 95), 30)
circle(Dom, (0, 0, 0), (350, 95), 30, 2)
circle(Dom, (255, 255, 255), (380, 95), 30)
circle(Dom, (0, 0, 0), (380, 95), 30, 2)
circle(Dom, (255, 255, 255), (410, 95), 30)
circle(Dom, (0, 0, 0), (410, 95), 30, 2)
circle(Dom, (255, 255, 255), (440, 95), 30)
circle(Dom, (0, 0, 0), (440, 95), 30, 2)

circle(Dom, (255, 255, 255), (380, 75), 30)
circle(Dom, (0, 0, 0), (380, 75), 30, 2)
circle(Dom, (255, 255, 255), (410, 75), 30)
circle(Dom, (0, 0, 0), (410, 75), 30, 2)


line(Dom, (1, 1, 1), (590, 135), (590, 300), 8) 

circle(Dom, (0, 120, 0), (550, 135), 30)
circle(Dom, (0, 0, 0), (550,135), 30, 2)
circle(Dom, (0, 120, 0), (630, 135), 30)
circle(Dom, (0, 0, 0), (630,135), 30, 2)
circle(Dom, (0, 120, 0), (590, 115), 30)
circle(Dom, (0, 0, 0), (590,115), 30, 2)
circle(Dom, (0, 120, 0), (560, 170), 30)
circle(Dom, (0, 0, 0), (560,170), 30, 2)
circle(Dom, (0, 120, 0), (620, 170), 30)
circle(Dom, (0, 0, 0), (620,170), 30, 2)
circle(Dom, (0, 120, 0), (590, 150), 30)
circle(Dom, (0, 0, 0), (590,150), 30, 2)


a = 20
b = 1.2*a
n = 24
alpha = 2*0.131
dots = list()
for i in range (n+1):
    xa = a*math.sin(alpha*i) + 600
    ya = a*math.cos(alpha*i) + 50 
    xb = b*math.sin(alpha*i) + 600
    yb = b*math.cos(alpha*i) + 50
    dots.append((xa, ya))
    dots.append((xb, yb))
polygon(screen, (255, 255, 0), dots, 0)

screen.blit(Dom, (0, 0))
Dom2 = pygame.transform.scale (Dom, (300, 200))
screen.blit(Dom2, (600, 200))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
