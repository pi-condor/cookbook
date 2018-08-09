import pygame
from player import Player

# Setup pygame
pygame.init()

# Create color constants
WHITE = (255, 255, 255)
BLACK = (255, 255, 255)

# Setup the display window
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Sprite Game :)')
game_display.fill(WHITE)
pygame.display.update()

# Setup the clock
FPS = 60
clock = pygame.time.Clock()

# Create a player
pirate = Player(game_display)

# Control variable
still_playing = True

# Game loop
while still_playing:
    # Clear the pygame events queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            still_playing = False
        
        # Move the pirate if they press down an arrow key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pirate.go_left()
            elif event.key == pygame.K_RIGHT:
                pirate.go_right()
        
        # Stop moving the pirate if they let go of an arrow key
        if event.type == pygame.KEYUP:
            # Stop moving the 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pirate.stop_moving()
    
    # Display the characters
    game_display.fill(WHITE)
    pirate.draw()
    pygame.display.update()

    clock.tick(60)

