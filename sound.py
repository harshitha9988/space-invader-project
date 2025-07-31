import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Background Image with Sound")


background_img = pygame.image.load("background.png")  
sound = pygame.mixer.Sound("background.wav.mp3")          

sound.play(-1) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.blit(background_img, (0, 0))
    pygame.display.flip()


pygame.quit()
sys.exit()