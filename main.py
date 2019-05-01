import math
import random
import pygame

from Evolution1.Graphics import WorldSim
from Evolution1.LifeForm import Life
from Evolution1.FoodForm import Food

def randomChance(d): # Boolean with a chance of 1/d of giving True
    rndNum = random.random()
    if rndNum <= 1/d:
        return True
    else:
        return False

print("Starting World")

# Definitions

speed = 100
width = 800
height = 600

#

world = WorldSim(width,height)
surface = world.surface
clock = world.clock

a = 0

def CreateLife():
    if randomChance(2):
        newLife = Life()
        x, y = random.randint(0, width), random.randint(0, height)
        newLife.Birth(surface, "Gen" + str(a), x, y, "red")
        print("Created: ", "Gen" + str(a), x, y)
def GrowFood():
    if randomChance(2):
        newFood = Food()
        x, y = random.randint(0, width), random.randint(0, height)
        newFood.Grow(surface, x, y, 1)
        print("Created: ", "Food", x, y)

# Events
evCreateLife = pygame.USEREVENT+1
evGrowFood = pygame.USEREVENT+2

pygame.time.set_timer(evCreateLife, 500)
pygame.time.set_timer(evGrowFood, 100)

Day = 0

while True:
    clock.tick(speed)
    for e in pygame.event.get():
        if e.type == evCreateLife:
            CreateLife()
        if e.type == evGrowFood:
            GrowFood()
    pygame.display.flip()