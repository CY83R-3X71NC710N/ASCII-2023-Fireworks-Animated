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
def draw_firework(x, y, color, radius, trail_color, trail_length):
    # Draw the trail
    pygame.draw.circle(screen, trail_color, (x, y), radius, trail_length)
    # Draw the firework
    pygame.draw.circle(screen, color, (x, y), radius)

# Load the stick figure image
stick_figure = pygame.image.load("stick_figure.png")
stick_figure_rect = stick_figure.get_rect()

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
    trail_color = (color[0]//2, color[1]//2, color[2]//2)
    trail_length = random.randint(5, 15)
    draw_firework(x, y, color, radius, trail_color, trail_length)

    # Draw the stick figure
    screen.blit(stick_figure, (x-stick_figure_rect.width, y-stick_figure_rect.height-30))

    # Update the screen
    pygame.display.flip()

    # Delay for a short time
    pygame.time.wait(100)

# Exit pygame
pygame.quit()
