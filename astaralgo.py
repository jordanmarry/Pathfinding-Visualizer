from queue import PriorityQueue
import pygame

from algoHelpers import *

def astar(draw, grid, start, end):

    for row in grid:
        for node in row:
            updateNeighbor(node, grid)

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