import sys
import pygame
from settings import *
from button import *


class Node:
    def __init__(self, row, col, width, total_rows, total_cols):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.x = row * width
        self.y = col * width
        self.color = WHITE
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
        self.color = LIGHT_BLUE

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

    def updateNeighbor(self, grid):
        self.neighbors = []
        # Goes Down
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].isWall():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].isWall():  # Goes Up
            self.neighbors.append(grid[self.row - 1][self.col])

        # Goes Right
        if self.col < self.total_cols - 1 and not grid[self.row][self.col + 1].isWall():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].isWall():  # Goes Left
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


class App:
    def __init__(self):
        self.grid_square_length = 24
        self.grid_row = 25
        self.grid_col = 50
        self.algo = ''
        self.running = True
        self.screen = WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Algorithm Visualizer")

    def run(self):
        self.screen.fill(WHITE)
        self.sketchTaskBar()
        grid = self.makeGrid()

        started = False

        start = None
        end = None

        while self.running:
            self.draw(grid)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if started:
                    continue

                # Left Click
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    row, col = self.getMousePos(pos)
                    try:
                        node = grid[row][col]

                        if not start and node != end:
                            start = node
                            start.makeStart()

                        elif not end and node != start:
                            end = node
                            end.makeEnd()

                        elif node != start and node != end:
                            node.makeWall()

                    except:
                        continue

                elif pygame.mouse.get_pressed()[2]:  # Right Mouse Button
                    pos = pygame.mouse.get_pos()
                    row, col = self.getMousePos(pos)
                    try:
                        node = grid[row][col]
                        node.resetNode()
                        if node == start:
                            start = None
                        elif node == end:
                            end = None
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

        self.dfsButton = Buttons(self, BLACK, ALGO_BUTTON_POSX, ALGO_BUTTON_POSY+60,
                                 ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Depth First Search')
        self.dfsButton.makeButton()

        self.bidirButton = Buttons(self, BLACK, ALGO_BUTTON_POSX*12, ALGO_BUTTON_POSY,
                                   ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Bidirectional Search')
        self.bidirButton.makeButton()

        self.dijButton = Buttons(self, BLACK, ALGO_BUTTON_POSX*12, ALGO_BUTTON_POSY+30,
                                 ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Dijkstra')
        self.dijButton.makeButton()

        self.gbfsButton = Buttons(self, BLACK, ALGO_BUTTON_POSX*12, ALGO_BUTTON_POSY+60,
                                  ALGO_BUTTON_LENGTH, ALGO_BUTTON_HEIGHT, 'Greedy Best First')
        self.gbfsButton.makeButton()

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

    # test
    def getMousePos(self, pos):
        y, x = pos

        row = y//self.grid_square_length
        col = x//self.grid_square_length

        return row, col
