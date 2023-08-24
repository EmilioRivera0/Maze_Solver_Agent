# necessary imports -------->
from json import load

# data structure declaration -------->
MAZE = []
PATH_STACK = []

# functions -------->
def load_maze():
    # local variables
    loaded_maze = []
    # maze extraction from json
    file = open("maze.json")
    temp_maze = load(file)["maze"]
    # serialization of loaded maze
    # top and bottom rows serialization
    for row_iterator in range(len(temp_maze[0])):
        if temp_maze[0][row_iterator] == 's':
            temp_maze[0][row_iterator] = 5
        elif temp_maze[0][row_iterator] == 'i':
            temp_maze[0][row_iterator] = 4
    for row_iterator in range(len(temp_maze[0])):
        if temp_maze[len(temp_maze)-1][row_iterator] == 's':
            temp_maze[len(temp_maze)-1][row_iterator] = 5
        elif temp_maze[len(temp_maze)-1][row_iterator] == 'i':
            temp_maze[len(temp_maze)-1][row_iterator] = 4
    # extreme left and right comuns serialization
    for column_iterator in range(len(temp_maze)):
        if temp_maze[column_iterator][0] == 's':
            temp_maze[column_iterator][0] = 5
        elif temp_maze[column_iterator][0] == 'i':
            temp_maze[column_iterator][0] = 4
    for column_iterator in range(len(temp_maze)):
        if temp_maze[column_iterator][len(temp_maze[0])-1] == 's':
            temp_maze[column_iterator][len(temp_maze[0])-1] = 5
        elif temp_maze[column_iterator][len(temp_maze[0])-1] == 'i':
            temp_maze[column_iterator][len(temp_maze[0])-1] = 4
    print(temp_maze)
    return temp_maze

def push_path_stack(coordinates):
    PATH_STACK.insert(0,coordinates)

def pop_path_stack():
    return PATH_STACK.pop(0)

load_maze()