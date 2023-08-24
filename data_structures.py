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
    Returns: MAZE, X_max, Y_max"""
    # maze extraction from json
    file = open("maze.json")
    temp_maze = load(file)["maze"]
    # initialize metadata variables
    X_max = len(temp_maze[0])
    Y_max = len(temp_maze)
    # serialization of loaded maze
    # top and bottom rows serialization
    for row_iterator in range(len(temp_maze[0])):
        if temp_maze[0][row_iterator] == 's':
            temp_maze[0][row_iterator] = 5
        elif temp_maze[0][row_iterator] == 'i':
            temp_maze[0][row_iterator] = 0
    for row_iterator in range(len(temp_maze[0])):
        if temp_maze[len(temp_maze)-1][row_iterator] == 's':
            temp_maze[len(temp_maze)-1][row_iterator] = 5
        elif temp_maze[len(temp_maze)-1][row_iterator] == 'i':
            temp_maze[len(temp_maze)-1][row_iterator] = 0
    # extreme left and right comuns serialization
    for column_iterator in range(len(temp_maze)):
        if temp_maze[column_iterator][0] == 's':
            temp_maze[column_iterator][0] = 5
        elif temp_maze[column_iterator][0] == 'i':
            temp_maze[column_iterator][0] = 0
    for column_iterator in range(len(temp_maze)):
        if temp_maze[column_iterator][len(temp_maze[0])-1] == 's':
            temp_maze[column_iterator][len(temp_maze[0])-1] = 5
        elif temp_maze[column_iterator][len(temp_maze[0])-1] == 'i':
            temp_maze[column_iterator][len(temp_maze[0])-1] = 0
    print(temp_maze)
    return temp_maze, X_max, Y_max

def push_path_stack(coordinates):
    """Push (x,y) coordinates to the PATH_STACK"""
    PATH_STACK.insert(0,coordinates)

def pop_path_stack():
    """Pop (x,y) coordinates from the PATH_STACK"""
    return PATH_STACK.pop(0)