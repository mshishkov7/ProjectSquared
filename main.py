
import pygame
import time
from random import randrange

#add detection of keypresses and some keys
from pygame.locals import (
    K_SPACE,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#init the game
pygame.init()

def GetRandomLocationOnScreen(x):
    r = randrange((x - 50))
    rangeCalc = int(r / 10)
    output = rangeCalc * 10
    return output

font = pygame.font.SysFont("Impact", 36)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
player_location_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
player_location_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)

endOfGameBool = False
wonLastRound = False

moveLenght = 10 #how much do you move when button pressed

cubeColor = ((randrange(50)), (randrange(255)), (randrange(255)))



entOfLevelLocation_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
entOfLevelLocation_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)


#def the screeen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#this will keep the main loop running
running = True

#Main Loop - everything in game is happening here
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT and (player_location_x > (SCREEN_WIDTH - SCREEN_WIDTH)) and endOfGameBool == False:
                print(player_location_x)
                player_location_x = player_location_x - moveLenght
                wonLastRound = False
            if event.key == K_RIGHT and (player_location_x < (SCREEN_WIDTH - 50)) and endOfGameBool == False:
                print(player_location_x)
                player_location_x = player_location_x + moveLenght 
                wonLastRound = False
            if event.key == K_UP and (player_location_y > (SCREEN_HEIGHT - SCREEN_HEIGHT)) and endOfGameBool == False:
                print(player_location_y)
                player_location_y = player_location_y - moveLenght  
                wonLastRound = False
            if event.key == K_DOWN and (player_location_y < (SCREEN_HEIGHT - 50)) and endOfGameBool == False:
                print(player_location_y)
                player_location_y = player_location_y + moveLenght  
                wonLastRound = False
        elif event.type == QUIT:
            running = False

    screen.fill('white') #we did create the screen var on line 21. now we change its color(fill it) with the RGB values of that color. pretty sure we can just type some of the colors like "black" or white
    
    surf = pygame.Surface((50, 50)) #creates a surface var, that is from the surf func of pygame. and we gave it size of 50 by 50
    surf.fill(cubeColor) #this new surface can be used as the screen surface, so we can change its color. now we make it white.
    rect = surf.get_rect() #get reckt lol.. we save the last surface in this rect var as a rectangular.
    
    endOfLevel = pygame.Surface((50, 50))
    endOfLevel.fill("red")   
    rect2 = endOfLevel.get_rect()
    
    #we can't just make the object and it magicaly apear on the screen, we need to assign it to diferent object, or in our case we will "blit" it to the screen.
    #blit() - stands for BLock Transfer, is how you copy the contents of one Surface to another.
    #You can only .blit() from one Surface to another, but since the screen is just another Surface, that’s not a problem.
    
    #surf_center = (
    #    (SCREEN_WIDTH - surf.get_width())/2,
    #    (SCREEN_HEIGHT - surf.get_height())/2
    #)
    #surf_center
    screen.blit(endOfLevel, (entOfLevelLocation_x, entOfLevelLocation_y))
    screen.blit(surf, (player_location_x, player_location_y)) #here we have the screen var from line 36. we "blit" it to the surf var, and we set the location on witch to draw - the center.

    if wonLastRound == True:
        txtsurf2 = font.render("You WON, try Again", True, (255,0,0))
        screen.blit(txtsurf2,(300, 50))
        cubeColor = ((randrange(255)), (randrange(255)), (randrange(255)))

    if player_location_x == entOfLevelLocation_x and player_location_y == entOfLevelLocation_y:
        endOfGameBool = True
        wonLastRound = True

    if endOfGameBool == False:
        txtsurf = font.render("Get to the red square!", True, (0,0,0))
        screen.blit(txtsurf,(10, 10))
    else:
        txtsurf = font.render("YOU WON!", True, (0,0,0))
        screen.blit(txtsurf,(250, 100))
        
        endOfGameBool = False
        entOfLevelLocation_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
        entOfLevelLocation_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)
        player_location_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
        player_location_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)



        
    
    pygame.display.flip()
    
    