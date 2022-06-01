"""
Python Data Structures - A Game-Based Approach
A Star Algorithm maze solver.

Uses a priority queue containing f-values and (i, j) tuples along with dictionaries for
predecessors and g-values.
"""

from helper import get_path, offsets, is_leg_position
from read_maze import read_maze
from priority_queue import PriorityQueue


def heuristic(a, b):
    """
    Calculates the Manhattan distance between two pairs of grid coordinates.
    (Calculate the distance/number of steps required from discovered node to goal node.)
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(_maze, _start, _goal):
    pq = PriorityQueue()
    preprocessor = {_start: None}
    g_value = {_start: 0}
    pq.put(_start, 0)

    while not pq.is_empty():
        current_pos = pq.get()
        if current_pos == _goal:
            return get_path(preprocessor, _start, _goal)
        for direction in ['up', 'right', 'down', 'left']:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_pos[0] + row_offset, current_pos[1] + col_offset)

            if is_leg_position(_maze, neighbour) and neighbour not in g_value:
                preprocessor[neighbour] = current_pos
                g_value[neighbour] = g_value[current_pos] + 1
                pq.put(neighbour, heuristic(_goal, neighbour))
    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    assert result is None
