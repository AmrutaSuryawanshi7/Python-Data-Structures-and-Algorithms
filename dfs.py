"""
Python Data Structures - A Game-Based Approach
DFS maze solver.

The stack contains positions as (row, column) tuples.
Predecessors are kept in a dictionary.
"""

from stack import Stack
from read_maze import read_maze
from helper import offsets, is_leg_position, get_path


def dfs(_maze, _start, _goal):
    stack = Stack()
    stack.push(_start)
    preprocessor = {_start: None}

    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == _goal:
            return get_path(preprocessor, _start, _goal)

        # Finding neighbours of current_cell
        for direction in ['up', 'right', 'down', 'left']:
            # Getting offsets position from offset dictionary
            row_offset, col_offset = offsets[direction]
            # Get neighbours position
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)

            if is_leg_position(_maze, neighbour) and neighbour not in preprocessor:
                stack.push(neighbour)
                preprocessor[neighbour] = current_cell
    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_dfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_dfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = dfs(maze, start_pos, goal_pos)
    assert result is None
