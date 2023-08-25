import time, os

def Sonny(maze):
    completed = False
    canMove = False
    stack = []
    #Identify start point
    row = 0
    for i in maze:
        if 'i' in i:
            column = i.index('i')
            maze[row][column] = 0
            stack.append([row, column])
            break
        row += 1
    '''
                    Directions
    Front,     Left,       Right,      Back
    -Row,      -Column,    +Column,    +Row
                    Values
    ^           <           >           v
    '''
    #Find the solution
    while((completed == False) and (len(stack) != 0)):
        #Print the maze in "real time" and the path followed by the agent
        os.system('cls')
        print("MAZE")
        printMaze(maze)
        print("Stack")
        print(stack)
        time.sleep(0.5)
        #Movementes available?
        if (maze[stack[-1][0]][stack[-1][1]] != 'v'):
            #Available to move to front
            #The current box is new
            if (maze[stack[-1][0]][stack[-1][1]] == 0):
                try:
                    #The box above is free
                    if (maze[stack[-1][0]-1][stack[-1][1]] == 0):
                        nextPosition = [stack[-1][0]-1, stack[-1][1]]
                        canMove = True
                    #Update information box
                    maze[stack[-1][0]][stack[-1][1]] = '^'
                    if (maze[stack[-1][0]-1][stack[-1][1]] == 5):
                        completed = True
                except:
                    canMove = False
            #Available to move to left
            #The current box has tried to move up
            elif (maze[stack[-1][0]][stack[-1][1]] == '^'):
                try:
                    #The box on the left is free
                    if (maze[stack[-1][0]][stack[-1][1]-1] == 0):
                        nextPosition = [stack[-1][0], stack[-1][1]-1]
                        canMove = True
                    #Update information box
                    maze[stack[-1][0]][stack[-1][1]] = '<'
                    if (maze[stack[-1][0]][stack[-1][1]-1] == 5):
                        completed = True
                except:
                    canMove = False
            #Available to move to right
            #The current box has tried to move to the left
            elif (maze[stack[-1][0]][stack[-1][1]] == '<'):
                try:
                    #The box on the right is free
                    if (maze[stack[-1][0]][stack[-1][1]+1] == 0):
                        nextPosition = [stack[-1][0], stack[-1][1]+1]
                        canMove = True
                    #Update information box
                    maze[stack[-1][0]][stack[-1][1]] = '>'
                    if (maze[stack[-1][0]][stack[-1][1]+1] == 5):
                        completed = True
                except:
                    canMove = False
            #Available to move to back
            #The current box has tried to move to the right
            elif (maze[stack[-1][0]][stack[-1][1]] == '>'):
                try:
                    #The box below is free
                    if (maze[stack[-1][0]+1][stack[-1][1]] == 0):
                        nextPosition = [stack[-1][0]+1, stack[-1][1]]
                        canMove = True
                    #Update information box
                    maze[stack[-1][0]][stack[-1][1]] = 'v'
                    if (maze[stack[-1][0]+1][stack[-1][1]] == 5):
                        completed = True
                except:
                    canMove = False
            
            #Move to the next box
            if (canMove):
                stack.append(nextPosition)
                canMove = False
        #The current box has tried to move in all direction
        else:
            maze[stack[-1][0]][stack[-1][1]] = '*'
            stack.pop()
    return row, column, completed, stack

def printMaze(maze):
    for i in maze:
        for j in i:
            print(str(j) + '\t', end="")
        print()

#main
# maze = [
#     [-1, -1,  5, -1, -1, -1],
#     [-1,  0,  0,   0,  0, -1],
#     [-1, -1, -1,  -1,  0, -1],
#     [-1,  0,  0,   0,  0, -1],
#     [-1,  0, -1,  -1,  -1, -1],
#     [-1,  0,  0,   0,  0,  -1],
#     [-1,  0,  0,   -1, 0, 'i'],
#     [-1, -1, -1,  -1,  -1, -1]
# ]

maze = [
    [-1,  5, -1, -1, -1, -1, -1, -1, -1],
    [-1,  0,  0,  0, -1,  0, -1, -1, -1],
    [-1,  0, -1, -1, -1,  0, -1,  0, -1],
    [-1,  0,  0,  0,  0,  0,  0,  0, -1],
    [-1,  0, -1, -1, -1,  0, -1,  0, -1],
    [-1, -1, -1,  0, -1, -1, -1,  0, -1],
    [-1,  0,  0,  0,  0, -1,  0,  0, -1],
    [-1,  0,  0,  0,  0,  0,  0,  0, -1],
    [-1, -1, -1, 'i',-1, -1, -1, -1, -1]
]

row, column, completed, stack = Sonny(maze)
if (completed):
    print("\nCompleted")
    print("Final maze")
    printMaze(maze)
    print("Final stack")
    print(stack)
else:
    print("\nThere is no solution")