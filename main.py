from sonny import *

# program execution -------->
MAZE, start_point = load_maze()
completed = Sonny(MAZE, start_point)
if (completed):
    print("\nCompleted")
    plt.imshow(MAZE, cmap='jet',interpolation='nearest')
    plt.show()
    os.system("clear")
    print("Final stack")
    print(PATH_STACK)
else:
    print("\nThere is no solution")
