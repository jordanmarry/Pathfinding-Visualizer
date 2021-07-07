import pygame

from algoHelpers import *



def dfs(draw, grid, start, end):
    queue = [start]
    visited = []
    prevNodes = {}

    for row in grid:
        for node in row:
            updateNeighbor(node, grid)

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        curr = queue.pop()
        
        if end in visited:
            reconstruct(prevNodes, end, draw)
            start.makeStart()
            end.makeEnd()
            return True
        
        visited.append(curr)
        for neighbor in curr.neighbors:
            prevNodes[neighbor] = curr
            queue.append(neighbor)
            neighbor.makeNeighbor()
            
        draw()
        
        if curr != start:
            curr.makeVisited()
    
    
    
    
    
    
    
    
    # for row in grid:
    #     for node in row:
    #         updateNeighbor(node, grid)
    
    # if end in visited:
    #     reconstruct(prevNodes, end, draw)
    #     start.makeStart()
    #     end.makeEnd()
    #     return True
    
    # if curr not in visited:
    #     visited.add(curr) 
    #     for neighbor in curr.neighbors:
    #         prevNodes[neighbor] = curr
    #         draw()
    #         if curr != start:
    #             curr.makeVisited()
    #         dfs(draw, grid, neighbor, start, end)
    
    
    

# def dfs(visited, graph, node):
#     if node not in visited:
#         print (node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)