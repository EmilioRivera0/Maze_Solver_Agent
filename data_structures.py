# necessary imports -------->
from json import load

# data structure declaration -------->
# matrix that will store the maze and the values for each coordinate
MAZE = []
# stack that will store the covered ground by the intelligent agent,
# givin him the ability to return to previous steps
PATH_STACK = []

# functions -------->
def load_maze():
    """Loads the maze contained by maze.json, initialize metadata values and makes a serialization process 
    to change the 's' and 'i' values to 5 and 4 respectively.
    Returns: MAZE, X_max, Y_max, start_point"""
    # maze extraction from json
    file = open("maze.json")
    temp_maze = load(file)["maze"]
    # declare and initialize metadata variables
    start_point = []
    X_max = len(temp_maze[0])
    Y_max = len(temp_maze)
    # serialization of loaded maze
    for row_iterator in range(len(temp_maze)):
        for column_iterator in range(len(temp_maze[row_iterator])):
            # s = exit
            if temp_maze[row_iterator][column_iterator] == 's':
                temp_maze[row_iterator][column_iterator] = 5
            # i = starting point
            elif temp_maze[row_iterator][column_iterator] == 'i':
                temp_maze[row_iterator][column_iterator] = 0
                # initialize the starting point
                start_point = [row_iterator,column_iterator]
    return temp_maze, X_max, Y_max, start_point

def push_path_stack(coordinates):
    """Push (x,y) coordinates to the PATH_STACK"""
    PATH_STACK.insert(0,coordinates)

def pop_path_stack():
    """Pop (x,y) coordinates from the PATH_STACK"""
    return PATH_STACK.pop(0)