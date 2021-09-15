import pygame

from algoHelpers import *

def bidir(draw, grid, start, end):
    for row in grid:
        for node in row:
            updateNeighbor(node, grid)
    
    endVisited = [end]
    endQueue = [end]
    endPrevNodes = {}

    startVisited = [start]
    startQueue = [start]
    startPrevNodes = {}
    
    while startQueue and endQueue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        curr2 = endQueue.pop(0)

        curr = startQueue.pop(0)

        if curr in endVisited:
            reconstruct(startPrevNodes, curr, draw)
            reconstruct(endPrevNodes, curr, draw)
            curr.makePath()
            start.makeStart()
            end.makeEnd()
            return True
        
        for neighbor in curr2.neighbors:
            if neighbor not in endVisited:
                endPrevNodes[neighbor] = curr2
                endVisited.append(neighbor)
                endQueue.append(neighbor)
                neighbor.makeNeighbor()

        for neighbor in curr.neighbors:
            if neighbor not in startVisited:
                startPrevNodes[neighbor] = curr
                startVisited.append(neighbor)
                startQueue.append(neighbor)
                neighbor.makeNeighbor()
                
        draw()
        
        if curr != start:
            curr.makeVisited()

        if curr2 != end:
            curr2.makeVisited()
    
    return False