import pygame
import pygame_gui
from pygame.locals import *
from pygame import mixer

#Background
pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('advventure image.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

# I honestly don't know
manager = pygame_gui.UIManager((800, 600))

#Button
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Say Hello',
                                            manager=manager)

#Music
mixer.init()
mixer.music.load('tunetank.com_1209_new-beginnings_by_romanov_studio.mp3')
mixer.music.play()

#Running
runing = True
while runing:
    window.blit(bg_img,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    pygame.display.update()
pygame.quit()

