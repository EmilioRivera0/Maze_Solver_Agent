import time, os

def Sonny(maze):
    completed = False
    canMove = False
    stack = []
    #Identify start point
    fila = 0
    for i in maze:
        if 'i' in i:
            columna = i.index('i')
            maze[fila][columna] = 0
            stack.append([fila, columna])
            break
        fila += 1
    '''
                    Directions
    Front,     Left,       Right,      Back
    -Row,      -Column,    +Column,    +Row
                    Values
    1           2           3           4
    '''
    while((completed == False) and (len(stack) != 0)):
        os.system('cls')
        printMaze(maze)
        time.sleep(1)
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
        else:
            #maze[stack[-1][0]][stack[-1][1]] = -1
            stack.pop()
    return fila, columna, completed

def printMaze(maze):
    for i in maze:
        for j in i:
            #print ("{:<4} {:<4} {:<4}".format('Name','Age','Percent'))
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

fila, columna, completed = Sonny(maze)
start = (fila, columna)
print("Start" + str(start))
if (completed):
    print("Completed")
else:
    print("There is no solution")
print("Final maze")
printMaze(maze)