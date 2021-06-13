import pygame

def updateNeighbor(node, grid):
    node.neighbors = []
    # Goes Down
    if node.row < node.total_rows - 1 and not grid[node.row + 1][node.col].isWall():
                node.neighbors.append(grid[node.row + 1][node.col])

    # Goes Up
    if node.row > 0 and not grid[node.row - 1][node.col].isWall():  
                node.neighbors.append(grid[node.row - 1][node.col])

    # Goes Right
    if node.col < node.total_cols - 1 and not grid[node.row][node.col + 1].isWall():
                node.neighbors.append(grid[node.row][node.col + 1])

    # Goes Left
    if node.col > 0 and not grid[node.row][node.col - 1].isWall():  
                node.neighbors.append(grid[node.row][node.col - 1])

def reconstruct(prevNodes, curr, draw):
    while curr in prevNodes:
        curr = prevNodes[curr]
        curr.makePath()
        draw()

def bfs(draw, grid, start, end):
    for row in grid:
        for node in row:
            updateNeighbor(node, grid)
            
    visited = []
    queue = []
    prevNodes = {}
    
    curr = start
    
    visited.append(curr)
    queue.append(curr)
    
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
            
            
    