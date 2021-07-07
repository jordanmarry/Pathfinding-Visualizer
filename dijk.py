import pygame

from algoHelpers import *

def dijk(draw, grid, start, end):
    for row in grid:
        for node in row:
            updateNeighbor(node, grid)