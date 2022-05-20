import pygame
import pygame_gui


pygame.init()

#Window
pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

#Background
width = 1000
height = 500
window = pygame.display.set_mode((width,height))
background = pygame.image.load('advventure image.png')
background = pygame.transform.scale(background,(width,height))

#UI Manager
manager = pygame_gui.UIManager((999,600), 'theme.json')

#Button
option1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30, 445), (940, 30)), text='Say Hello', manager=manager)
option2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30, 415), (940, 30)), text='Say Hello', manager=manager)
option3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30, 385), (940, 30)), text='Say Hello', manager=manager)
option4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30, 355), (940, 30)), text='Say Hello', manager=manager)
#Clock
clock = pygame.time.Clock()
is_running = True

#Running
while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)

#Button Function
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == option1:
                print('Hello World!')

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()



