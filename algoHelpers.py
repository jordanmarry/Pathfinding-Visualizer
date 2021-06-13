# Makes neighbors for all of the nodes

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

# Makes the path from the end to start

def reconstruct(prevNodes, curr, draw):
    while curr in prevNodes:
        curr = prevNodes[curr]
        curr.makePath()
        draw()
        
# A* Star Algo

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)