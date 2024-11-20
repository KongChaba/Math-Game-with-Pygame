import pygame 

# screen = screen
# button_rect => 

class Button:
    def __init__(self, width, height, color, hover_color=None):
        self.width = width
        self.height = height
        self.color = color
        self.current_color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.font = pygame.font.Font(r'font\Matrixtype.ttf', 48)
        self.rect = None

    def check_hover(self, rect):
        # Check if mouse is over the button
        mouse_pos = pygame.mouse.get_pos()
        self.is_hovered = rect.collidepoint(mouse_pos)

    def draw(self, screen, x, y, text):
        self.rect = pygame.Rect(x, y, self.width, self.height)

        if self.hover_color != None:
            self.check_hover(self.rect)
            self.current_color = self.hover_color if self.is_hovered else self.color

        # Draw the button  
        pygame.draw.rect(screen, pygame.Color(self.current_color), self.rect)

        # Render text
        text_surface = self.font.render(text, True, pygame.Color("black"))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)