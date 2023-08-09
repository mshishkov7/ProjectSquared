import pygame
from random import randrange


def GetRandomLocationOnScreen(xy):
    r = randrange((xy - 50))
    rangeCalc = int(r / 10)
    output = rangeCalc * 10
    return output

def getCenter(SCREEN_WIDTH, SCREEN_HEIGHT, surface1):
    x = (SCREEN_WIDTH - surface1.get_width())/2
    y = (SCREEN_HEIGHT - surface1.get_height())/2
    return (x, y)

def CreateListOfFiresAndLocations(SCREEN_WIDTH, SCREEN_HEIGHT, j):
    xfire = GetRandomLocationOnScreen(SCREEN_WIDTH)
    yfire = GetRandomLocationOnScreen(SCREEN_HEIGHT)
    if yfire < 60:
        yfire = 70
    i = 0
    listOfFires = [(xfire, yfire)]
    while i < j-1:  # Corrected loop condition |||| 
        xfire = GetRandomLocationOnScreen(SCREEN_WIDTH)
        yfire = GetRandomLocationOnScreen(SCREEN_HEIGHT)
        if yfire < 60:
            yfire = 70
            
        listOfFires.append((xfire, yfire))
        i += 1
    return listOfFires
        
