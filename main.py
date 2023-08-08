import pygame
from random import randrange

#add detection of keypresses and some keys
from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,
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

def getCenter(SCREEN_WIDTH, SCREEN_HEIGHT, surface1):
    x = (SCREEN_WIDTH - surface1.get_width())/2
    y = (SCREEN_HEIGHT - surface1.get_height())/2
    return (x, y)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

hero1 = "hero1-50x50.png"
hero2 = "hero2-50x50.png"
hero3 = "hero3-50x50.png"
hero4 = "hero4-50x50.png"
currentHeroPlayer1 = hero1
isHeroSellectedPlayer1 = False
currentHeroPlayer2 = hero2
isHeroSellectedPlayer2 = False

font = pygame.font.SysFont("Impact", 26)
font_Rockwell = pygame.font.SysFont("Rockwell", 20)
font_Rubik = pygame.font.SysFont("Rubik", 50)

player1_location_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
player1_location_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)
if player1_location_y <60:
    player1_location_y = 70
player2_location_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
player2_location_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)
if player2_location_y <60:
    player2_location_y = 70

endOfGameBool = False
winnerLastRound = False
winState = False
moveLenght = 10 #how much do you move when button pressed

cubeColor = ((randrange(50)), (randrange(255)), (randrange(255)))

entOfLevelLocation_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
entOfLevelLocation_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)
if entOfLevelLocation_y < 60:
    entOfLevelLocation_y = 70

player1Lives = 5
player2Lives = 5
lastWinner = ""
winnerIs = ""

topBorder = pygame.Surface((SCREEN_WIDTH + 20, 50))
topBorder.fill("#696E96")   
rect2 = topBorder.get_rect()

#def the screeen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#this will keep the main loop running
isThereAWinner = False
running = True

##############Choose a hero for player 1 loop
while running and isHeroSellectedPlayer1 == False:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT and (player1_location_x > (SCREEN_WIDTH - SCREEN_WIDTH)) and endOfGameBool == False:
                currentHeroPlayer1 = hero1
                isHeroSellectedPlayer1 = True
            if event.key == K_RIGHT and (player1_location_x < (SCREEN_WIDTH - 50)) and endOfGameBool == False:
                currentHeroPlayer1 = hero2
                isHeroSellectedPlayer1 = True
            if event.key == K_UP and (player1_location_y > (SCREEN_HEIGHT - SCREEN_HEIGHT)) and endOfGameBool == False:
                currentHeroPlayer1 = hero3
                isHeroSellectedPlayer1 = True
            if event.key == K_DOWN and (player1_location_y < (SCREEN_HEIGHT - 50)) and endOfGameBool == False:
                currentHeroPlayer1 = hero4
                isHeroSellectedPlayer1 = True
            if event.key == K_r:
                endOfGameBool = True
        elif event.type == QUIT:
            running = False
    screen.fill("#5DA299") 
    
    screen.blit(topBorder, (0, 0))
    
    chooseAHeroTxt = font.render("Player 1 choose a hero UP/Down/Left/Right", True, (0,0,0))
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
##############Choose a hero for player 2 loop
while running and isHeroSellectedPlayer2 == False:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_a and (player2_location_x > (SCREEN_WIDTH - SCREEN_WIDTH)) and endOfGameBool == False:
                currentHeroPlayer2 = hero1
                isHeroSellectedPlayer2 = True
            if event.key == K_d and (player2_location_x < (SCREEN_WIDTH - 50)) and endOfGameBool == False:
                currentHeroPlayer2 = hero2
                isHeroSellectedPlayer2 = True
            if event.key == K_w and (player2_location_y > (SCREEN_HEIGHT - SCREEN_HEIGHT)) and endOfGameBool == False:
                currentHeroPlayer2 = hero3
                isHeroSellectedPlayer2 = True
            if event.key == K_s and (player2_location_y < (SCREEN_HEIGHT - 50)) and endOfGameBool == False:
                currentHeroPlayer2 = hero4
                isHeroSellectedPlayer2 = True
            if event.key == K_r:
                endOfGameBool = True
        elif event.type == QUIT:
            running = False
    screen.fill("#1854e7") 
    
    screen.blit(topBorder, (0, 0))
     
    chooseAHeroTxt = font.render("Player 2 choose a hero W/A/S/D", True, (0,0,0))
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
while running and isThereAWinner == False:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT and (player1_location_x > (SCREEN_WIDTH - SCREEN_WIDTH)) and endOfGameBool == False:
                print(player1_location_x)
                player1_location_x = player1_location_x - moveLenght
                winnerLastRound = False
            if event.key == K_RIGHT and (player1_location_x < (SCREEN_WIDTH - 50)) and endOfGameBool == False:
                print(player1_location_x)
                player1_location_x = player1_location_x + moveLenght 
                winnerLastRound = False
            if event.key == K_UP and (player1_location_y > (SCREEN_HEIGHT - SCREEN_HEIGHT + 50)) and endOfGameBool == False:
                print(player1_location_y)
                player1_location_y = player1_location_y - moveLenght  
                winnerLastRound = False
            if event.key == K_DOWN and (player1_location_y < (SCREEN_HEIGHT - 50)) and endOfGameBool == False:
                print(player1_location_y)
                player1_location_y = player1_location_y + moveLenght  
                winnerLastRound = False
            if event.key == K_a and (player2_location_x > (SCREEN_WIDTH - SCREEN_WIDTH)) and endOfGameBool == False:
                print(player2_location_x)
                player2_location_x = player2_location_x - moveLenght
                winnerLastRound = False
            if event.key == K_d and (player2_location_x < (SCREEN_WIDTH - 50)) and endOfGameBool == False:
                print(player2_location_x)
                player2_location_x = player2_location_x + moveLenght 
                winnerLastRound = False
            if event.key == K_w and (player2_location_y > (SCREEN_HEIGHT - SCREEN_HEIGHT + 50)) and endOfGameBool == False:
                print(player2_location_y)
                player2_location_y = player2_location_y - moveLenght  
                winnerLastRound = False
            if event.key == K_s and (player2_location_y < (SCREEN_HEIGHT - 50)) and endOfGameBool == False:
                print(player2_location_y)
                player2_location_y = player2_location_y + moveLenght  
                winnerLastRound = False
            if event.key == K_r:
                endOfGameBool = True
        elif event.type == QUIT:
            running = False

    screen.fill((87,178,77)) #we did create the screen var on line 21. now we change its color(fill it) with the RGB values of that color. pretty sure we can just type some of the colors like "black" or white
    
    screen.blit(topBorder, (0, 0))
    
    #player1 = pygame.Surface((50, 50)) #creates a surface var, that is from the player1 func of pygame. and we gave it size of 50 by 50
    #player1.fill(cubeColor) #this new surface can be used as the screen surface, so we can change its color. now we make it white.
    #rect = player1.get_rect() #get reckt lol.. we save the last surface in this rect var as a rectangular.
    
    player1 = pygame.image.load(currentHeroPlayer1)
    player2 = pygame.image.load(currentHeroPlayer2)
    endOfLevel = pygame.image.load("finish.png")
    #endOfLevel = pygame.Surface((50, 50))
    #endOfLevel.fill("red")   
    #rect2 = endOfLevel.get_rect()
    
    #we can't just make the object and it magicaly apear on the screen, we need to assign it to diferent object, or in our case we will "blit" it to the screen.
    #blit() - stands for BLock Transfer, is how you copy the contents of one Surface to another.
    #You can only .blit() from one Surface to another, but since the screen is just another Surface, that’s not a problem.
    
    #surf_center = (
    #    (SCREEN_WIDTH - player1.get_width())/2,
    #    (SCREEN_HEIGHT - player1.get_height())/2
    #)
    #surf_center
    
    screen.blit(endOfLevel, (entOfLevelLocation_x, entOfLevelLocation_y))
    screen.blit(player1, (player1_location_x, player1_location_y)) #here we have the screen var from line 36. we "blit" it to the player1 var, and we set the location on witch to draw - the center.
    screen.blit(player2, (player2_location_x, player2_location_y))

    player1LivesTxt = font_Rockwell.render("Player 1 Lives: " + str(player1Lives), True, (0,0,0))
    player2LivesTxt = font_Rockwell.render("Player 2 Lives: " + str(player2Lives), True, (0,0,0))
    
    screen.blit(player1LivesTxt,(300, 15))
    screen.blit(player2LivesTxt,(580, 15))
    
    if winnerLastRound == True:
        txtsurf2 = font.render("Player " + lastWinner + "won last round", True, (255,0,0))
        screen.blit(txtsurf2,(300, 50))
        cubeColor = ((randrange(255)), (randrange(255)), (randrange(255)))

    if (player1_location_x == entOfLevelLocation_x and player1_location_y == entOfLevelLocation_y):
        endOfGameBool = True
        winnerLastRound = True
        player2Lives = player2Lives - 1
        lastWinner = "1"
        
    if (player2_location_x == entOfLevelLocation_x and player2_location_y == entOfLevelLocation_y):
        endOfGameBool = True
        winnerLastRound = True
        player1Lives = player1Lives - 1
        lastWinner = "2"
    
    if endOfGameBool == False:
        txtsurf = font.render("Get to the red square first!", True, (0,0,0))
        screen.blit(txtsurf,(10, 10))
    if endOfGameBool == True:
        endOfGameBool = False
        entOfLevelLocation_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
        entOfLevelLocation_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)
        if entOfLevelLocation_y < 60:
            entOfLevelLocation_y = 70
            
        # after every round reset the players location on the screen
        #player1_location_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
        #player1_location_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)
        #if player1_location_y <60:
        #    player1_location_y = 70
        #player2_location_x = GetRandomLocationOnScreen(SCREEN_WIDTH)
        #player2_location_y = GetRandomLocationOnScreen(SCREEN_HEIGHT)
        #if player2_location_y <60:
        #    player2_location_y = 70
        
    if player1Lives == 0:
        print("lives are 0 for player 1")
        isThereAWinner = True
        winnerIs = "Player 2"
    if player2Lives == 0:
        print("lives are 0 for player 2")
        isThereAWinner = True
        winnerIs = "Player 2"
        
    
    pygame.display.flip()

while running and isThereAWinner == True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_r:
                endOfGameBool = True
                isThereAWinner = False
        elif event.type == QUIT:
            running = False
    
    screen.fill("#BF5840") 
    
    screen.blit(topBorder, (0, 0))
    
    theWinnerIs = font_Rubik.render(winnerIs + " is the winner", True, (0,0,0))
    screen.blit(theWinnerIs, (getCenter(SCREEN_WIDTH, SCREEN_HEIGHT, theWinnerIs)))

    pressR = font_Rockwell.render("Press R to reset", True, (0,0,0))
    screen.blit(pressR, (300,15))
    
    pygame.display.flip()