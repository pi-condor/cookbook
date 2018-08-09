import pygame
import time
import sys

pygame.init()

# Colors
black = (0,0,0)
white = (255,255,255)

# Setup the display window
width = 800
height = 500
game_display = pygame.display.set_mode((width, height))
game_display.fill(white)
pygame.display.set_caption('A bit racey...')

# Setup the clock (used to calculate FPS)
clock = pygame.time.Clock()

# Render car graphics
class Car():
    def __init__(self):
        self.img = pygame.image.load('img/racecar.png')
        self.rect = self.img.get_rect()
        self.width = self.rect.size[0]
        self.x = width * 0.45 # The x location of the top-left pixel
        self.y = height * 0.8 # The y location of the top-left pixel
    
    def update_position(self):
        self.constrain_x()

    def change_x_by(self, change_in_x):
        self.x += change_in_x

    def draw(self):
        """Blit the car to the location (self.x, self.y)"""
        # Blit "draws the image to the display," but the image won't appear until the display is updated
        self.update_position()
        game_display.blit(self.img, (self.x, self.y))
    
    def constrain_x(self):
        """Prevent the player from moving off screen"""
        self.x = max(0, min(self.x, width - self.width))

# Render text
def get_text_objects(msg, font, color):
    """Return the text objects needed to display a given message"""
    textSurface = font.render(msg, True, color)
    return textSurface, textSurface.get_rect()

def display_message(msg, pos, font_size = 80, color = (0, 0, 0)):
    """Display a message centered at the given position (x, y) on a display"""
    font_face = pygame.font.Font('freesansbold.ttf', font_size)
    text_surface, text_rect = get_text_objects(msg, font_face, color)
    text_rect.center = pos
    game_display.blit(text_surface, text_rect)

def introduce_game():
    display_message("Welcome to my game!", (width / 2, height / 2))
    pygame.display.update()

def game_loop():
    crashed = False

    user_car = Car()

    while not crashed:
        # Check the events queue to prevent the program from freezing
        for event in pygame.event.get():
            # Exit the loop if you 'x' out of the window
            if event.type == pygame.QUIT:
                crashed = True
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    print("Scrolling up!")
                elif event.button == 4:
                    print("Scrolling down!")
                sys.stdout.flush()

        # Update the x position of the car
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            user_car.change_x_by(-5)
        if pressed_keys[pygame.K_RIGHT]:
            user_car.change_x_by(5)
        
        # Update the entire display window and set the fps to 60
        game_display.fill(white)
        user_car.draw()
        pygame.display.update()
        clock.tick(60)

introduce_game()
time.sleep(2)
game_loop()
pygame.quit()