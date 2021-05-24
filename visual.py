import pygame
import math
import algorithms.astar

from pygame.constants import GL_GREEN_SIZE


WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Algorithm Visualizer")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHT_BLUE = (60, 150, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        
    def getPos (self):
        return self.row, self.col
    
    def isVisited (self):
        return self.color == BLUE
    
    def isNeighbor (self):
        return self.color == LIGHT_BLUE
    
    def isWall (self):
        return self.color == BLACK
    
    def isStart (self):
        return self.color == GREEN
    
    def isEnd (self):
        return self.color == RED
    
    def resetNode (self):
        self.color = WHITE
    
    def makeVisited (self):
        self.color = BLUE
        
    def makeNeighbor (self):
        self.color = LIGHT_BLUE
    
    def makeWall (self):
        self.color = BLACK
        
    def makeStart (self):
        self.color = GREEN
        
    def makeEnd (self):
        self.color = RED
        
    def makePath (self):
        self.color = YELLOW
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def updateNeighbor(self, grid):
        pass
    
    def __lt__ (self, other):
        return False
    
def h (p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def makeGrid (rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
            
    return grid

def drawGrid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))
            
def draw(win, grid, rows, width):
    win.fill(WHITE)
    
    for row in grid:
        for node in row:
            node.draw(win)
            
    drawGrid(win, rows, width)
    pygame.display.update()
    
def getClickedPos(pos, rows, width):
    gap = width // rows
    y, x = pos
    
    row = y // gap
    col = x // gap
    
    return row, col

def main (win, width):
    ROWS = 50
    grid = makeGrid(ROWS, width)
    
    start = None
    end = None
    
    run = True
    started = False
    
    while run:
        draw(win, grid, ROWS, width)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if started:
                continue
            
            if pygame.mouse.get_pressed()[0]: #Left Mouse Button
                pos = pygame.mouse.get_pos()
                row, col = getClickedPos(pos, ROWS, width)
                node = grid[row][col]
                
                if not start and node != end:
                    start = node
                    start.makeStart()
                    
                elif not end and node != start:
                    end = node
                    end.makeEnd()
                
                elif node != start and node != end:
                    node.makeWall()
                
            elif pygame.mouse.get_pressed()[2]: # Right Mouse Button
                pos = pygame.mouse.get_pos()
                row, col = getClickedPos(pos, ROWS, width)
                node = grid[row][col]
                node.resetNode()
                if node == start:
                    start = None
                elif node == end:
                    end = None
                            
    pygame.quit()

main(WIN, WIDTH)