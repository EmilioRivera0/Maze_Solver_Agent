# necessary imports -------->
import time
import os
from data_structures import *

# functions -------->
def Sonny(maze, start_point):
    '''
                    Directions
    Front,     Left,       Right,      Back
    -Row,      -Column,    +Column,    +Row
                    Values
    ^           <           >           v
    '''
    # local variables
    completed = False
    canMove = False
    current_position = []
    # initialize PATH_STACK with starting point
    push_path_stack(start_point)
    print(PATH_STACK)
    #Find the solution
    while((completed == False) and (len(PATH_STACK) != 0)):
        #Print the maze in "real time" and the path followed by the agent
        os.system('cls')
        print("MAZE")
        printMaze(maze)
        print("Stack")
        print(PATH_STACK)
        time.sleep(0.05)
        # initialize current position
        current_position = get_stack_top()
        print(current_position)
        #Movementes available?
        if (maze[current_position[0]][current_position[1]] != 'v'):
            #Available to move to front
            #The current box is new
            if (maze[current_position[0]][current_position[1]] == 0):
                try:
                    #The box above is free
                    if (maze[current_position[0]-1][current_position[1]] == 0):
                        nextPosition = [current_position[0]-1, current_position[1]]
                        canMove = True
                    #Update information box
                    maze[current_position[0]][current_position[1]] = '^'
                    if (maze[current_position[0]-1][current_position[1]] == 5):
                        completed = True
                except:
                    canMove = False
            #Available to move to left
            #The current box has tried to move up
            elif (maze[current_position[0]][current_position[1]] == '^'):
                try:
                    #The box on the left is free
                    if (maze[current_position[0]][current_position[1]-1] == 0):
                        nextPosition = [current_position[0], current_position[1]-1]
                        canMove = True
                    #Update information box
                    maze[current_position[0]][current_position[1]] = '<'
                    if (maze[current_position[0]][current_position[1]-1] == 5):
                        completed = True
                except:
                    canMove = False
            #Available to move to right
            #The current box has tried to move to the left
            elif (maze[current_position[0]][current_position[1]] == '<'):
                try:
                    #The box on the right is free
                    if (maze[current_position[0]][current_position[1]+1] == 0):
                        nextPosition = [current_position[0], current_position[1]+1]
                        canMove = True
                    #Update information box
                    maze[current_position[0]][current_position[1]] = '>'
                    if (maze[current_position[0]][current_position[1]+1] == 5):
                        completed = True
                except:
                    canMove = False
            #Available to move to back
            #The current box has tried to move to the right
            elif (maze[current_position[0]][current_position[1]] == '>'):
                try:
                    #The box below is free
                    if (maze[current_position[0]+1][current_position[1]] == 0):
                        nextPosition = [current_position[0]+1, current_position[1]]
                        canMove = True
                    #Update information box
                    maze[current_position[0]][current_position[1]] = 'v'
                    if (maze[current_position[0]+1][current_position[1]] == 5):
                        completed = True
                except:
                    canMove = False
            
            #Move to the next box
            if (canMove):
                push_path_stack(nextPosition)
                canMove = False
        #The current box has tried to move in all direction
        else:
            maze[current_position[0]][current_position[1]] = '*'
            pop_path_stack()
    return completed

def printMaze(maze):
    for i in maze:
        for j in i:
            print(str(j) + '\t', end="")
        print()


# program execution -------->
MAZE, start_point = load_maze()
completed = Sonny(MAZE, start_point)
if (completed):
    print("\nCompleted")
    print("Final maze")
    printMaze(MAZE)
    print("Final stack")
    print(PATH_STACK)
else:
    print("\nThere is no solution")