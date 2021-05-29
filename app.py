import sys
import pygame
from settings import *
from button import *


class App:
    def __init__(self):
        self.grid_square_length = 24
        self.algo = ''
        self.running = True
        self.screen = WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Algorithm Visualizer")
        self.start_node_x = None
        self.start_node_y = None
        self.end_node_x = None
        self.end_node_y = None
    
    def run(self):
        while self.running:
            self.sketchTaskBar()
            self.sketchGraph()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()
    
    def sketchTaskBar(self):
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen, LIGHT_BLUE, (0, 0, WIDTH, 125), 0)
        
        self.astarButton = Buttons(self, BLACK, ALGO_BUTTON_POSX, ALGO_BUTTON_POSY, ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'A* Search')
        self.astarButton.makeButton()
        
        self.bfsButton = Buttons(self, BLACK, ALGO_BUTTON_POSX, ALGO_BUTTON_POSY*2.5, ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Breadth First Search')
        self.bfsButton.makeButton()
        
        self.dfsButton = Buttons(self, BLACK, ALGO_BUTTON_POSX, ALGO_BUTTON_POSY*4, ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Depth First Search')
        self.dfsButton.makeButton()
        
        self.bidirButton = Buttons(self, BLACK, ALGO_BUTTON_POSX*12, ALGO_BUTTON_POSY, ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Bidirectional Search')
        self.bidirButton.makeButton()
        
        self.dijButton = Buttons(self, BLACK, ALGO_BUTTON_POSX*12, ALGO_BUTTON_POSY*2.5, ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Dijkstra')
        self.dijButton.makeButton()
        
        self.gbfsButton = Buttons(self, BLACK, ALGO_BUTTON_POSX*12, ALGO_BUTTON_POSY*4, ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Greedy Best First')
        self.gbfsButton.makeButton()
        
        self.clearButton = Buttons(self, BLACK, (WIDTH - 200), 125//2.75, ALGO_BUTTON_LENGTH*.75, ALGO_BUTTON_HEIGHT*1.5, 'Clear')
        self.clearButton.makeButton()
        
        self.visualButton = Buttons(self, INDIGO, (WIDTH - 150)//2, (125)//2.75, ALGO_BUTTON_LENGTH*.75, ALGO_BUTTON_HEIGHT*1.5, 'Visualize')
        self.visualButton.makeButton()
        
        pygame.display.update()
        
    def sketchGraph(self):
        pass
        
        
    