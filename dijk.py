import pygame

from algoHelpers import *

def dijk(draw, grid, start, end):
    for row in grid:
        for node in row:
            updateNeighbor(node, grid)

    visited = [start]
    queue = [start]
    prevNodes = {}

    curr = start

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        curr = queue.pop(0)

        if end in visited:
            reconstructDij(prevNodes, end, draw)
            start.makeStart()
            end.makeEnd()
            
            return True
        
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                if curr == start:
                    prevNodes[neighbor] = (curr, 1)
                else:
                    prevNodes[neighbor] = (curr, prevNodes[curr][1] + neighbor.weight)
                visited.append(neighbor)
                queue.append(neighbor)
                neighbor.makeNeighbor()

        draw()
        
        if curr != start:
            curr.makeVisited()