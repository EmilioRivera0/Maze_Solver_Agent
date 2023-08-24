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
    1           2           3           4
    '''
    eliminado = []
    while((completed == False) and (len(stack) != 0)):
        os.system('cls')
        print("MAZE")
        printMaze(maze)
        print("Stack")
        print(stack)
        time.sleep(0.5)
        #Movementes available?
        if (maze[stack[-1][0]][stack[-1][1]] < 4):
            #Available to move to front
            if (maze[stack[-1][0]][stack[-1][1]] == 0):
                try:
                    if (maze[stack[-1][0]-1][stack[-1][1]] == 0):
                        nextPosition = [stack[-1][0]-1, stack[-1][1]]
                        canMove = True
                    if (maze[stack[-1][0]-1][stack[-1][1]] == 5):
                        completed = True
                except:
                    canMove = False
            #Available to move to left
            elif (maze[stack[-1][0]][stack[-1][1]] == 1):
                try:
                    if (maze[stack[-1][0]][stack[-1][1]-1] == 0):
                        nextPosition = [stack[-1][0], stack[-1][1]-1]
                        canMove = True
                    if (maze[stack[-1][0]][stack[-1][1]-1] == 5):
                        completed = True
                except:
                    canMove = False
            #Available to move to right
            elif (maze[stack[-1][0]][stack[-1][1]] == 2):
                try:
                    if (maze[stack[-1][0]][stack[-1][1]+1] == 0):
                        nextPosition = [stack[-1][0], stack[-1][1]+1]
                        canMove = True
                    if (maze[stack[-1][0]][stack[-1][1]+1] == 5):
                        completed = True
                except:
                    canMove = False
            #Available to move to back
            elif (maze[stack[-1][0]][stack[-1][1]] == 3):
                try:
                    if (maze[stack[-1][0]+1][stack[-1][1]] == 0):
                        nextPosition = [stack[-1][0]+1, stack[-1][1]]
                        canMove = True
                    if (maze[stack[-1][0]+1][stack[-1][1]] == 5):
                        completed = True
                except:
                    canMove = False
            #Update information box
            maze[stack[-1][0]][stack[-1][1]] += 1
            #Move to next box
            if (canMove):
                stack.append(nextPosition)
                canMove = False
        else:
            #maze[stack[-1][0]][stack[-1][1]] = 8
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