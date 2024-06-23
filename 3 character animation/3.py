import pygame

# always intialize pygame
pygame.init() 

# create a window where we will draw on 

#screen attribute
screen_width = 825
screen_height = 480

win = pygame.display.set_mode( (screen_width,screen_height) ) # input as a tuple of (width,height)
pygame.display.set_caption('First Game') # setting caption 

# load multiple images in pygame
# pygame.path.join('data','l1.png') for joining images in other folders
walkRight = [pygame.image.load('3 character animation\R1.png'), pygame.image.load('3 character animation\R2.png'), pygame.image.load('3 character animation\R3.png'), pygame.image.load('3 character animation\R4.png'), pygame.image.load('3 character animation\R5.png'), pygame.image.load('3 character animation\R6.png'), pygame.image.load('3 character animation\R7.png'), pygame.image.load('3 character animation\R8.png'), pygame.image.load('3 character animation\R9.png')]
walkLeft = [pygame.image.load('3 character animation\L1.png'), pygame.image.load('3 character animation\L2.png'), pygame.image.load('3 character animation\L3.png'), pygame.image.load('3 character animation\L4.png'), pygame.image.load('3 character animation\L5.png'), pygame.image.load('3 character animation\L6.png'), pygame.image.load('3 character animation\L7.png'), pygame.image.load('3 character animation\L8.png'), pygame.image.load('3 character animation\L9.png')]
bg = pygame.image.load('3 character animation\\bg.jpg')
char = pygame.image.load('3 character animation\standing.png')

#clock for frmaes 
clock = pygame.time.Clock()

# charateristics of out rectangular object
x = 50
y = 400
width = 64  # sprite hieght and width
height = 64 
vel = 5

#character animaiton and sprite
left = False
right = False
walkCount = 0

# for jumping 
isJump = False
jumpCount = 10

    
def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0)) # load image in the bg at 0,0 coordinate
    
    # draw an image 
    if walkCount + 1 >= 27: #bc we have 9 strides of images and each stride will get 3 frames, so 9*3 = 27
        walkCount = 0
    
    if left:
        win.blit(walkLeft[walkCount//3],(x,y))
        walkCount+=1
    elif right:
        win.blit(walkRight[walkCount//3],(x,y))
        walkCount+=1
    else:
        win.blit(char,(x,y))
    
    pygame.display.update() # refresh the display / to show something on the display 

# main loop to run the game
run = True
while run:
    clock.tick(27)
    # pygame.event.get() gives a list of all the events happend
    for event in pygame.event.get(): # event is anything from key presses to mouse click
        if event.type == pygame.QUIT:
            run = False
            
    # for moving the rectangle
    keys = pygame.key.get_pressed()
    
    # see the grid in pygames
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_width-width-vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
        
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount**2) * 0.5 * neg # a quadratic function for jumping 
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
    
    redrawGameWindow()


pygame.quit() # ends the program and closes the window