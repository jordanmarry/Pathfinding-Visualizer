import pygame

from algoHelpers import *

def bfs(draw, grid, start, end):
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
            reconstruct(prevNodes, end, draw)
            start.makeStart()
            end.makeEnd()
            return True
        
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                prevNodes[neighbor] = curr
                visited.append(neighbor)
                queue.append(neighbor)
                neighbor.makeNeighbor()
                
        draw()
        
        if curr != start:
            curr.makeVisited()
            
            
    