import pygame

from algoHelpers import *

def bidir(draw, grid, start, end):
    for row in grid:
        for node in row:
            updateNeighbor(node, grid)