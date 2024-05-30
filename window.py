import pygame
import sys
from buttons import *
from play_music import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def is_button_clicked(button_rect, mouse_pos):
    return button_rect.collidepoint(mouse_pos)

pygame.init()

screen_width = 1300
screen_height = 690
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Audio Player')

icon = pygame.image.load('music.png')
pygame.display.set_icon(icon)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            rect = pygame.Rect(300, 250, 200, 100)
            if is_button_clicked(rect, mouse_pos):
                print("Button clicked!")


    screen.fill((255, 255, 255))
    rect = pygame.Rect(300, 250, 200, 100)
    button_icon_size = (40, 40)
    button_radius = 20
    Playbutton(screen,WHITE,rect,button_radius,icon='music.png',icon_size=button_icon_size)

    pygame.display.flip()

pygame.quit()
sys.exit()
