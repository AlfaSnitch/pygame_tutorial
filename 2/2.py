import pygame

# always intialize pygame
pygame.init() 

# create a window where we will draw on 

win = pygame.display.set_mode( (500,500) ) # input as a tuple of (width,height)
pygame.display.set_caption('First Game') # setting caption 

#screen attribute
screen_width = 500
screen_height = 500

# charateristics of out rectangular object
x = 50
y = 450
width = 40
height = 60
vel = 5

# for jumping 
isJump = False
jumpCount = 10

# main loop to run the game
run = True
while run:
    pygame.time.delay(50)
    # pygame.event.get() gives a list of all the events happend
    for event in pygame.event.get(): # event is anything from key presses to mouse click
        if event.type == pygame.QUIT:
            run = False
            
    # for moving the rectangle
    keys = pygame.key.get_pressed()
    
    # see the grid in pygames
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500-width-vel:
        x += vel
    if not isJump:
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500-height-vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount**2) * 0.5 * neg
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
    
    win.fill((0,0,0)) # fills the screen with black color
    
    # draw rectangle -- see pygame website for drawing other shapes(circle)
    pygame.draw.rect(win, (255,0,0), (x,y, width ,height)) #(surface,color,rect)
    pygame.display.update() # refresh the display / to show something on the display 

pygame.quit() # ends the program and closes the window