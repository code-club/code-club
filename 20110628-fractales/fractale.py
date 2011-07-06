import pygame
from julia import julia_fract

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
 
pygame.init()
  
# Set the height and width of the screen
size=[700,700]
screen=pygame.display.set_mode(size)
 
pygame.display.set_caption("Fractale")
 
#Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()


#jf = julia_fract(0.4+0.2j, 100)
jf = julia_fract(0.2 - 0.5j, 100)
pixels = jf.computeJulia(size)
#pixels = jf.computeMandelbrot(size)

pygame.display.flip()

# -------- Main Program Loop -----------
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # Set the screen background
    
    for x in xrange(0, size[0]):
        for y in xrange(0, size[1]):
            #print julia[(x,y)]
            screen.set_at((x, y), (35 + pixels[x,y], 135 + pixels[x,y] ,  155 + pixels[x,y]))
      
    print 'tick'
    # screen.fill(black)
    break 
    # Limit to 20 frames per second
    clock.tick(1)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
