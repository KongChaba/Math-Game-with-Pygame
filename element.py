import pygame

class Text:
    def __init__(self, color, font_size, style=None):
        self.color = color
        self.font_size = font_size
        self.style = style

    def set(self, text):
        font = pygame.font.Font(r'font\Matrixtype.ttf', self.font_size)

        if self.style == "bold":
            font.set_bold(True)
        elif self.style == "italic":
            font.set_italic(True)
        
        txt = font.render(text, True, self.color)
        return txt
    
style_1 = Text(color='black', font_size=80, style='bold')
style_2 = Text(color='white', font_size=52, style='bold')
style_3 = Text(color='black', font_size=42)