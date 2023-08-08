
import pygame
import time
from random import randrange

#add detection of keypresses and some keys
from pygame.locals import (
    K_r,
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

def GetRandomLocationOnScreen(xy):
    r = randrange((xy - 50))
    rangeCalc = int(r / 10)
    output = rangeCalc * 10
    return output

hero1 = "hero1-50x50.png"
hero2 = "hero2-50x50.png"
hero3 = "hero3-50x50.png"
hero4 = "hero4-50x50.png"
currentHero = hero1
isHeroSelected = False

font = pygame.font.SysFont("Impact", 36)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
player_location_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
player_location_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)

endOfGameBool = False
wonLastRound = False
winState = False
moveLenght = 10 #how much do you move when button pressed

cubeColor = ((randrange(50)), (randrange(255)), (randrange(255)))

entOfLevelLocation_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
entOfLevelLocation_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)

#def the screeen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#this will keep the main loop running
running = True

#Choose a hero Loop
while running and isHeroSelected == False:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT and (player_location_x > (SCREEN_WIDTH - SCREEN_WIDTH)) and endOfGameBool == False:
                currentHero = hero1
                isHeroSelected = True
            if event.key == K_RIGHT and (player_location_x < (SCREEN_WIDTH - 50)) and endOfGameBool == False:
                currentHero = hero2
                isHeroSelected = True
            if event.key == K_UP and (player_location_y > (SCREEN_HEIGHT - SCREEN_HEIGHT)) and endOfGameBool == False:
                currentHero = hero3
                isHeroSelected = True
            if event.key == K_DOWN and (player_location_y < (SCREEN_HEIGHT - 50)) and endOfGameBool == False:
                currentHero = hero4
                isHeroSelected = True
            if event.key == K_r:
                endOfGameBool = True
        elif event.type == QUIT:
            running = False
    screen.fill("#5DA299") #we did create the screen var on line 21. now we change its color(fill it) with the RGB values of that color. pretty sure we can just type some of the colors like "black" or white
    
    chooseAHeroTxt = font.render("Choose a Hero with UP/Down/Left/Right", True, (0,0,0))
    screen.blit(chooseAHeroTxt,(10, 10))
    
    chooseImgHero1 = pygame.image.load("hero1-200x200.png")
    chooseImgHero2 = pygame.image.load("hero2-200x200.png")
    chooseImgHero3 = pygame.image.load("hero3-200x200.png")
    chooseImgHero4 = pygame.image.load("hero4-200x200.png")
    arrowsImg = pygame.image.load("arrow.png")
    
    screen.blit(chooseImgHero1, (75, 200))
    screen.blit(chooseImgHero2, (525, 200))
    screen.blit(chooseImgHero3, (300, 50))
    screen.blit(chooseImgHero4, (300, 400))
    
    arrow_x = 300
    arrow_y = 200
    
    screen.blit(arrowsImg, (arrow_x, arrow_y))
    
    pygame.display.flip()
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
            if event.key == K_r:
                endOfGameBool = True
        elif event.type == QUIT:
            running = False

    screen.fill((87,178,77)) #we did create the screen var on line 21. now we change its color(fill it) with the RGB values of that color. pretty sure we can just type some of the colors like "black" or white
    
    #surf = pygame.Surface((50, 50)) #creates a surface var, that is from the surf func of pygame. and we gave it size of 50 by 50
    #surf.fill(cubeColor) #this new surface can be used as the screen surface, so we can change its color. now we make it white.
    #rect = surf.get_rect() #get reckt lol.. we save the last surface in this rect var as a rectangular.
    
    surf = pygame.image.load(currentHero)
    endOfLevel = pygame.image.load("finish.png")
    #endOfLevel = pygame.Surface((50, 50))
    #endOfLevel.fill("red")   
    #rect2 = endOfLevel.get_rect()
    
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
    if endOfGameBool == True:
        endOfGameBool = False
        entOfLevelLocation_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
        entOfLevelLocation_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)
        player_location_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
        player_location_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)

    pygame.display.flip()
    
    