from queue import PriorityQueue
import pygame


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)


def reconstruct(prevNodes, curr, draw):
    while curr in prevNodes:
        curr = prevNodes[curr]
        curr.makePath()
        draw()


def astar(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    prevNodes = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.getPos(), end.getPos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        curr = open_set.get()[2]
        open_set_hash.remove(curr)

        if curr == end:
            reconstruct(prevNodes, end, draw)
            start.makeStart()
            end.makeEnd()
            return True

        for neighbor in curr.neighbors:
            temp_g_score = g_score[curr] + 1

            if temp_g_score < g_score[neighbor]:
                prevNodes[neighbor] = curr
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + \
                    h(neighbor.getPos(), end.getPos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.makeNeighbor()

        draw()

        if curr != start:
            curr.makeVisited()

    return False

def updateNeighbor(node, grid):
    print("WE IN HERE LIKE SWIMWEAR")
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