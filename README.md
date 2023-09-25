# Maze Solver Intelligent Agent

Intelligent Agent called Sonny capable of solving mazes represented in a matrices. Where: 
- -1 rerpesents a wall
- 0 represents a not covered coordinate
- 1 represents that Sonny already checked the upward coordinate 
- 2 represents that Sonny already checked the upward and left coordinates
- 3 represents that Sonny already checked the upward, left and right coordinates
- 4 represents that Sonny already checked the upward, left, right and inferior coordinates
- 5 represents that all the coordinate's neighboring where checked (will never be checked again)
- 6/'s' represents the exit of the maze
- 'i' represents the starting point of the maze
- Each coordinate occupies one element of the matrix
- The matrix must be square (same length for x and y dimensions)
## maze.json
The program can solve any maze that is specified in the maze.json and fulfills the previous rules.
## Comments
The new implementation of displays Sonny's movements and walkthrough the maze until the program finds a solution or Sonny covers all the possible paths.
Although this new implementation enables graphical visualization, it has problems with the performance of the agent due to the constant rendering of the maze.
## Authors

- [@EmilioRivera0](https://github.com/EmilioRivera0)
- [@JuanPabloGHC](https://github.com/JuanPabloGHC)
