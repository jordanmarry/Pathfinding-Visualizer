import sys
import pygame
from settings import *
from button import *
from astaralgo import *
from bfs import *
from dfs import *
from dijk import *
from bidir import *


class Node:
    def __init__(self, row, col, width, total_rows, total_cols):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_cols
        self.total_cols = total_rows
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.gridCopy = None
        self.weight = 1
        self.neighbors = []

    def getPos(self):
        return self.row, self.col

    def isVisited(self):
        return self.color == BLUE

    def isNeighbor(self):
        return self.color == LIGHT_BLUE

    def isWall(self):
        return self.color == BLACK

    def isStart(self):
        return self.color == GREEN

    def isEnd(self):
        return self.color == RED

    def resetNode(self):
        self.color = WHITE

    def makeVisited(self):
        self.color = BLUE

    def makeNeighbor(self):
        self.color = DARK_BLUE

    def makeWall(self):
        self.color = BLACK

    def makeStart(self):
        self.color = GREEN

    def makeEnd(self):
        self.color = RED

    def makePath(self):
        self.color = YELLOW

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def __lt__(self, other):
        return False


class App:
    def __init__(self):
        self.grid_square_length = 24
        self.grid_row = 25
        self.grid_col = 50
        self.algo = ""
        self.running = True
        self.screen = WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Algorithm Visualizer")

    def run(self):
        self.screen.fill(WHITE)
        self.sketchTaskBar()
        grid = self.makeGrid()

        started = False
        executed = False

        start = None
        startWas = False
        end = None
        endWas = False

        while self.running:
            self.draw(grid)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if started:
                    continue

                if executed:
                    self.clearButton.color = GREEN
                    self.clearButton.makeButton()
                    self.visualButton.color = INDIGO
                    self.visualButton.makeButton()

                # Left Click
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    row, col = self.getMousePos(pos)
                    try:
                        node = grid[row][col]

                        if not start and node != end :
                            start = node
                            start.makeStart()
                            if end != None and startWas ==  True and self.algo != "":
                                self.visualButton.color = GREEN
                                self.visualButton.makeButton()
                            startWas = True
                        
                        elif not end and node != start:
                            end = node
                            end.makeEnd()
                            if start != None and endWas == True and self.algo != "":
                                self.visualButton.color = GREEN
                                self.visualButton.makeButton()
                            endWas = True
                        
                        elif node != start and node != end and start and end and self.clearButton.color != GREEN:
                            node.makeWall()

                    except:
                        row, col = pos
                        #
                        # Clear Button
                        #    
                                    
                        if row >= 850 and row <= 1000 and col >= 665 and col <= 700:
                            start = None
                            end = None
                            grid = self.makeGrid()
                            self.sketchTaskBar()
                            executed = False
                            self.algo = ""

                        elif start != None and end != None and started != True and executed != True:
                            try:
                                print(row, col)
                                

                                #
                                # A Star Search Button
                                #

                                if row >= 20 and row <= 220 and col >= 640 and col <= 660:
                                    self.algo = "astar"
                                    self.sketchTaskBar()
                                    self.astarButton.color = GREEN
                                    self.astarButton.makeButton()
                                    self.visualButton.color = GREEN
                                    self.visualButton.makeButton()
                                    print(self.algo)
                                
                                #
                                # BFS Button
                                #
                                
                                elif row >= 20 and row <= 220 and col >= 670 and col <= 690:
                                    self.algo = "bfs"
                                    self.sketchTaskBar()
                                    self.bfsButton.color = GREEN
                                    self.bfsButton.makeButton()
                                    self.visualButton.color = GREEN
                                    self.visualButton.makeButton()
                                    print(self.algo)
                               
                                #
                                # DFS Button
                                #    
                                    
                                elif row >= 120 and row <= 320 and col >= 700 and col <= 720:
                                    self.algo = "dfs"
                                    self.sketchTaskBar()
                                    self.dfsButton.color = GREEN
                                    self.dfsButton.makeButton()
                                    self.visualButton.color = GREEN
                                    self.visualButton.makeButton()
                                    print(self.algo)
                                
                                #
                                # BiDir Search Button
                                #    
                                    
                                elif row >= 240 and row <= 440 and col >= 640 and col <= 660:
                                    self.algo = "bidir"
                                    self.sketchTaskBar()
                                    self.bidirButton.color = GREEN
                                    self.bidirButton.makeButton()
                                    self.visualButton.color = GREEN
                                    self.visualButton.makeButton()
                                    print(self.algo)
                                
                                #
                                # Dijkstra Button
                                #    
                                    
                                elif row >= 240 and row <= 440 and col >= 670 and col <= 690:
                                    self.algo = "dijk"
                                    self.sketchTaskBar()
                                    self.dijButton.color = GREEN
                                    self.dijButton.makeButton()
                                    self.visualButton.color = GREEN
                                    self.visualButton.makeButton()
                                    print(self.algo)

                                #
                                # Visual Button
                                #

                                elif row >= 525 and row <= 675 and col >= 665 and col <= 695:
                                    if self.visualButton.color == GREEN:
                                        started = True
                                        executed = True
                                        
                                        #
                                        # A Star Search
                                        #
                                        
                                        if self.algo == "astar":
                                            if astar(lambda: self.draw(grid), grid, start, end):
                                                started = False
                                                continue
                                            else:
                                                started = False
                                                continue   

                                        #
                                        # BFS Search
                                        #

                                        elif self.algo == "bfs":
                                            if bfs(lambda: self.draw(grid), grid, start, end):
                                                started = False
                                                continue
                                            else:
                                                started = False
                                                continue

                                        #
                                        # DFS Search
                                        #

                                        elif self.algo == "dfs":
                                            if dfs(lambda: self.draw(grid), grid, start, end):
                                                started = False
                                                continue
                                            else:
                                                started = False
                                                continue

                                        #
                                        # Bidir Search
                                        #

                                        elif self.algo == "bidir":
                                            if bidir(lambda: self.draw(grid), grid, start, end):
                                                started = False
                                                continue
                                            else:
                                                started = False
                                                continue

                                        #
                                        # dijk Search
                                        #

                                        elif self.algo == "dijk":
                                            if dijk(lambda: self.draw(grid), grid, start, end):
                                                started = False
                                                continue
                                            else:
                                                started = False
                                                continue


                            except:
                                continue
                        else:
                            continue

                elif pygame.mouse.get_pressed()[2]:  # Right Mouse Button
                    pos = pygame.mouse.get_pos()
                    row, col = self.getMousePos(pos)
                    try:
                        if executed != True:
                            node = grid[row][col]
                            node.resetNode()
                            if node == start:
                                start = None
                                self.visualButton.color = INDIGO
                                self.visualButton.makeButton()
                            elif node == end:
                                end = None
                                self.visualButton.color = INDIGO
                                self.visualButton.makeButton()
                    except:
                        continue

        pygame.quit()

    def sketchTaskBar(self):
        pygame.draw.rect(self.screen, LIGHT_BLUE, (0, 600, WIDTH, 168))

        self.astarButton = Buttons(self, BLACK, ALGO_BUTTON_POSX, ALGO_BUTTON_POSY,
                                   ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'A* Search')
        self.astarButton.makeButton()

        self.bfsButton = Buttons(self, BLACK, ALGO_BUTTON_POSX, ALGO_BUTTON_POSY+30,
                                 ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Breadth First Search')
        self.bfsButton.makeButton()

        self.dfsButton = Buttons(self, BLACK, ALGO_BUTTON_POSX*6, ALGO_BUTTON_POSY+60,
                                 ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Depth First Search')
        self.dfsButton.makeButton()

        self.bidirButton = Buttons(self, BLACK, ALGO_BUTTON_POSX*12, ALGO_BUTTON_POSY,
                                   ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Bidirectional Search')
        self.bidirButton.makeButton()

        self.dijButton = Buttons(self, BLACK, ALGO_BUTTON_POSX*12, ALGO_BUTTON_POSY+30,
                                 ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Dijkstra')
        self.dijButton.makeButton()

        self.clearButton = Buttons(self, BLACK, (WIDTH - 350), 665,
                                   ALGO_BUTTON_LENGTH*.75, ALGO_BUTTON_HEIGHT*1.5, 'Clear')
        self.clearButton.makeButton()

        self.visualButton = Buttons(self, INDIGO, (WIDTH - 150)//2, 665,
                                    ALGO_BUTTON_LENGTH*.75, ALGO_BUTTON_HEIGHT*1.5, 'Visualize')
        self.visualButton.makeButton()

        pygame.display.update()

    def makeGrid(self):
        grid = []
        for i in range(self.grid_col):
            grid.append([])
            for j in range(self.grid_row):
                node = Node(i, j, self.grid_square_length,
                            self.grid_row, self.grid_col)
                grid[i].append(node)

        return grid

    def sketchGrid(self):
        for col in range(self.grid_col):
            pygame.draw.line(self.screen, BLACK, (GS_X + col*self.grid_square_length,
                             GS_Y), (GS_X + col*self.grid_square_length, GE_Y))
        for row in range(self.grid_row):
            pygame.draw.line(self.screen, BLACK, (GS_X, GS_Y + row *
                             self.grid_square_length), (GE_X, GS_Y + row*self.grid_square_length))

    def draw(self, grid):
        for row in grid:
            for node in row:
                node.draw(self.screen)

        self.sketchGrid()
        pygame.display.update()

    def getMousePos(self, pos):
        y, x = pos

        row = y//self.grid_square_length
        col = x//self.grid_square_length

        return row, col
