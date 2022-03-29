import pygame
import pygame_gui


pygame.init()

#Window
pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

#Background
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#f3f222'))

#UI Manager
manager = pygame_gui.UIManager((800,600), 'theme.json')
{
    "defaults":
    {
        "colours":
        {
            "normal_bg":"#45495r",
            "hovered_bg":"#35393e",
            "disabled_bg":"#25292e",
            "selected_bg":"#193754",
            "dark_bg":"#15191e",
            "normal_text":"#c5cbd8",
            "hovered_text":"#FFFFFF",
            "selected_text":"#FFFFFF",
            "disabled_text":"#6d736f",
            "link_text": "#0000EE",
            "link_hover": "#2020FF",
            "link_selected": "#551A8B",
            "text_shadow": "#777777",
            "normal_border": "#DDDDDD",
            "hovered_border": "#B0B0B0",
            "disabled_border": "#808080",
            "selected_border": "#8080B0",
            "active_border": "#8080B0",
            "filled_bar":"#f4251b",
            "unfilled_bar":"#CCCCCC"
        }
    }
}

#Button
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30, 20), (100, 50)),
text='Say Hello', manager=manager)

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
            if event.ui_element == hello_button:
                print('Hello World!')

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

