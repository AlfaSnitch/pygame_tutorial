import pygame

# always intialize pygame
pygame.init() 

# create a window where we will draw on 

win = pygame.display.set_mode( (500,500) ) # input as a tuple of (width,height)
pygame.display.set_caption('First Game') # setting caption 

# charateristics of out rectangular object
x = 50
y = 50
width = 40
height = 60
vel = 5

# main loop to run the game
run = True
while run:
    pygame.time.delay(100)
    # pygame.event.get() gives a list of all the events happend
    for event in pygame.event.get(): # event is anything from key presses to mouse click
        if event.type == pygame.QUIT:
            run = False
            
    # for moving the rectangle
    keys = pygame.key.get_pressed()
    
    # see the grid in pygames
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    
    win.fill((0,0,0)) # fills the screen with black color
    
    # draw rectangle -- see pygame website for drawing other shapes(circle)
    pygame.draw.rect(win, (255,0,0), (x,y, width ,height)) #(surface,color,rect)
    pygame.display.update() # refresh the display / to show something on the display 

pygame.quit() # ends the program and closes the window