"""
Python Data Structures and Algorithms - A Game-Based Approach
Helper functions and values for use with other files in this project.
"""

offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


def is_leg_position(maze, pos):
    i, j = pos
    num_row = len(maze)
    num_col = len(maze[0])
    return 0 <= i < num_row and 0 <= j < num_col and maze[i][j] != "*"


def get_path(preprocessor, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = preprocessor[current]
    path.append(start)
    path.reverse()
    return path
