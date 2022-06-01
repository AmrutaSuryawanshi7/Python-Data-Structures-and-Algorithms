"""
Python Data Structures - A Game-Based Approach
BFS maze solver.

The queue contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

from helper import get_path, offsets, is_leg_position
from read_maze import read_maze
from queue_ll import Queue


def bfs(_maze, _start, _goal):
    queue = Queue()
    queue.enqueue(_start)
    preprocessor = {_start: None}

    while not queue.is_empty():
        current_position = queue.dequeue()

        if current_position == _goal:
            return get_path(preprocessor, _start, _goal)

        for direction in ['up', 'right', 'down', 'left']:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_position[0] + row_offset, current_position[1] + col_offset)
            if is_leg_position(_maze, neighbour) and neighbour not in preprocessor:
                queue.enqueue(neighbour)
                preprocessor[neighbour] = current_position
    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None
