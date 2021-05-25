from settings import *

class Buttons():
    def __init__(self, app, color, x, y, width, height, text=''):
        self.app = app
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        
    def makeButton(self):
        pygame.draw.rect(self.app.screen, self.color, (self.x, self.y, self.width, self.height), 0)
        font = pygame.font.Font(None, 25)
        text = font.render(self.text, 1, WHITE)
        self.app.screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    
    