import pygame
import random

# Initialize pygame
pygame.init()

# Set screen size and caption
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fireworks")

# Create a list of colors for the fireworks
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

# Create a function to draw a firework
def draw_firework(x, y, color, radius):
    pygame.draw.circle(screen, color, (x, y), radius)

# Main loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw a random firework at a random location
    x = random.randint(50, 650)
    y = random.randint(50, 450)
    color = random.choice(colors)
    radius = random.randint(10, 50)
    draw_firework(x, y, color, radius)
    
    # Update the screen
    pygame.display.flip()
    
    # Delay for a short time
    pygame.time.wait(100)
    
# Exit pygame
pygame.quit()
