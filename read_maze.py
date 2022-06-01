"""
Python Data Structures - A Game-Based Approach
Reading a maze from a text file
"""


def read_maze(file_name):
    """
    Reads a maze stored in a text file and returns a 2d list containing the maze representation.
    """
    try:
        with open(file_name) as file:
            # list comprehension
            maze = [[char for char in line.strip("\n")] for line in file]
            num_of_rows_means_total_col = len(maze[0])

            for row in maze:
                # print(row)
                if len(row) != num_of_rows_means_total_col:
                    print("The maze is not rectangular.")
                    raise SystemExit
            return maze

    except OSError:
        print("There is a problem with the file you have selected.")
        raise SystemExit


if __name__ == "__main__":
    _maze = read_maze("mazes/modest_maze.txt")
    for _row in _maze:
        print(_row)

    print("\n--------------------------------------\n")

    _maze = read_maze("mazes/challenge_maze.txt")
    for _row in _maze:
        print(_row)
