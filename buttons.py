import pygame

BLACK = (0, 0, 0)

def Playbutton(surface, color, rect, radius, icon=None,icon_size=None):

    pygame.draw.rect(surface, color, rect, border_radius=radius)

    if icon:
        icon = pygame.image.load(icon)
        if icon_size:
            icon = pygame.transform.scale(icon, icon_size)  # Resize the icon
        icon_rect = icon.get_rect(center=rect.center)
        surface.blit(icon, icon_rect)