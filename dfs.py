import pygame

from algoHelpers import *

def dfs(draw, grid, start, end):
    for row in grid:
        for node in row:
            updateNeighbor(node, grid)
            
    visited = []
    queue = []
    prevNodes = {}
    
    curr = start

    queue.append(curr)
    

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        curr = queue.pop()
        
        visited.append(curr)

        if end in visited:
            reconstruct(prevNodes, end, draw)
            start.makeStart()
            end.makeEnd()
            return True
        
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                prevNodes[neighbor] = curr
                queue.append(neighbor)
                neighbor.makeNeighbor()
            
        draw()
        
        if curr != start:
            curr.makeVisited()