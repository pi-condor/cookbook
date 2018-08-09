import pygame
import time

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, game_display):
        # Initialize a pygame sprite
        super().__init__()

        # Bring in the game display from pygame (so we can draw onto it)
        self.game_display = game_display

        # Create arrays to store the images for each walking animation
        # The right images will be the same as the left ones, just flipped
        self.images_left  = []
        self.images_right = []

        # Add sprites to the right image array
        self.images_right.append(pygame.image.load('forward1-pirate.png'))
        self.images_right.append(pygame.image.load('forward2-pirate.png'))

        # Add sprites to the left image array
        for image in self.images_right:
            # Pygame.transform.flip takes in an image, and two booleans
            # If the first boolean is True, the image is flipped horizontally
            # If the second boolean is True, the image is flipped vertically
            # So all we're doing is horizontally flipping each image from self.images_right
            flipped_image = pygame.transform.flip(image, True, False)
            self.images_left.append(flipped_image)

        # Add the stationary images for the Pirate
        self.right_still_image = pygame.image.load('stationary-pirate.png')
        self.left_still_image = pygame.transform.flip(self.right_still_image, True, False)

        # Make the pirate face right at the beginning of the program
        self.current_image = self.right_still_image

        # Get the rect of the object (for positioning purposes)
        self.rect = self.current_image.get_rect()

        # Center the player on the point 400, 400
        self.rect.center = (400, 400)

        # Set the change in x every frame
        self.change_in_x = 0

        # Create a variable to store which way the character is facing
        self.orientation = "right"
    
        # Store the last time the frame was updated
        self.time_of_last_sprite_change = time.time()

        # Store which animation frame we're on
        self.frame = 0
    
    def draw(self): 
        # Draw the player to the screen, after updating their sprite and poisition
        self.update_sprite()
        self.move()
        self.game_display.blit(self.current_image, self.rect)
    
    def update_sprite(self):
        # If the player isn't moving, display the correct still image
        if self.change_in_x == 0:
            if self.orientation == "left":
                self.current_image = self.left_still_image
            elif self.orientation == "right":
                self.current_image = self.right_still_image

        # Otherwise, step through the walking animation
        else:
            self.pick_frame()

            # Pick the correct image from the list based on the current frame and the orientation of the player
            if self.orientation == "left":
                self.current_image = self.images_left[self.frame]
            elif self.orientation == "right":
                self.current_image = self.images_right[self.frame]

    def move(self):
        # Move the character horizontally based on its self.change_in_x variable
        self.rect.move_ip(self.change_in_x, 0)

    def go_right(self):
        # Update the time since the last sprite change
        self.time_of_last_sprite_change = time.time()

        # Advance the player to the right
        self.change_in_x = 10
        self.orientation = "right"
    
    def go_left(self):
        # Update the time since the last sprite change
        self.time_of_last_sprite_change = time.time()

        # Advance the player to the right
        self.change_in_x = -10
        self.orientation = "left"
    
    def stop_moving(self):
        self.change_in_x = 0

    def pick_frame(self):
        # If it's been more than 0.15 seconds since the frame was last updated, update the frame
        if time.time() - self.time_of_last_sprite_change > 0.15:
            self.time_of_last_sprite_change = time.time()
            if self.frame == 0:
                self.frame = 1
            else:
                self.frame = 0
            
