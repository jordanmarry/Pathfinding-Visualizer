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
            node.updateNeighbor(node, grid)
            
    
            
    