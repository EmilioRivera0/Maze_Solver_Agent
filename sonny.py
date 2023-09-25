# necessary imports -------->
import time
import matplotlib.pyplot as plt
from data_structures import *

# functions -------->
def Sonny(maze, start_point):
    '''
                    Directions
    Front,     Left,       Right,      Back
    -Row,      -Column,    +Column,    +Row
                    Values
    1           2           3           4
    '''
    # local variables
    completed = False
    canMove = False
    current_position = []
    # initialize PATH_STACK with starting point
    push_path_stack(start_point)
    #Find the solution
    while((completed == False) and (len(PATH_STACK) != 0)):
        #Render the maze in "real time" and the path followed by the agent
        os.system("clear")
        print('Path Stack:\n', PATH_STACK)
        plt.imshow(maze, cmap='jet',interpolation='nearest')
        plt.pause(0.001)
        plt.clf()
        # initialize current position
        current_position = get_stack_top()
        #Movementes available?
        if (maze[current_position[0]][current_position[1]] < 4):
            #Available to move to front
            #The current box is new
            if (maze[current_position[0]][current_position[1]] == 0):
                try:
                    #The box above is free
                    if (maze[current_position[0]-1][current_position[1]] == 0):
                        nextPosition = [current_position[0]-1, current_position[1]]
                        canMove = True
                    #Update information box
                    maze[current_position[0]][current_position[1]] = 1
                    if (maze[current_position[0]-1][current_position[1]] == 6):
                        completed = True
                        print("Completed Front")
                except:
                    canMove = False
            #Available to move to left
            #The current box has tried to move up
            elif (maze[current_position[0]][current_position[1]] == 1):
                try:
                    #The box on the left is free
                    if (maze[current_position[0]][current_position[1]-1] == 0):
                        nextPosition = [current_position[0], current_position[1]-1]
                        canMove = True
                    #Update information box
                    maze[current_position[0]][current_position[1]] = 2
                    if (maze[current_position[0]][current_position[1]-1] == 6):
                        completed = True
                        print("Completed Left")
                except:
                    canMove = False
            #Available to move to right
            #The current box has tried to move to the left
            elif (maze[current_position[0]][current_position[1]] == 2):
                try:
                    #The box on the right is free
                    if (maze[current_position[0]][current_position[1]+1] == 0):
                        nextPosition = [current_position[0], current_position[1]+1]
                        canMove = True
                    #Update information box
                    maze[current_position[0]][current_position[1]] = 3
                    if (maze[current_position[0]][current_position[1]+1] == 6):
                        completed = True
                        print("Completed Right")
                except:
                    canMove = False
            #Available to move to back
            #The current box has tried to move to the right
            elif (maze[current_position[0]][current_position[1]] == 3):
                try:
                    #The box below is free
                    if (maze[current_position[0]+1][current_position[1]] == 0):
                        nextPosition = [current_position[0]+1, current_position[1]]
                        canMove = True
                    #Update information box
                    maze[current_position[0]][current_position[1]] = 4
                    if (maze[current_position[0]+1][current_position[1]] == 6):
                        completed = True
                        print("Completed Below")
                except:
                    canMove = False
            
            #Move to the next box
            if (canMove):
                push_path_stack(nextPosition)
                canMove = False
        #The current box has tried to move in all direction
        else:
            maze[current_position[0]][current_position[1]] = 5
            pop_path_stack()
    return completed
