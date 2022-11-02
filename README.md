# GameOfLife
## Conway’s Game Of Life (Python Implementation using the multiplication property of Matrix)

### Problem:

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

    Any live cell with fewer than two live neighbours dies, as if by loneliness.
    Any live cell with more than three live neighbours dies, as if by overcrowding.
    Any live cell with two or three live neighbours lives, unchanged, to the next generation.
    Any dead cell with exactly three live neighbours comes to life.

The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed - births and deaths happen simultaneously, and the discrete moment at which this happens is sometimes called a tick. (In other words, each generation is a pure function of the one before.) The rules continue to be applied repeatedly to create further generations. '''

### Solution:

For testing the app, run main.py and follow the remaining procedures as printed in the console during execution.

#### Sample input and output:

------------------------------------------------------------------------------------------------------------------
Input A:
(Block pattern - Still life)
1, 1
1, 2
2, 1
2, 2
Output A:
1, 1
1, 2
2, 1
2, 2
--------------------------------------------------------------------------------------------- ---------------------
Input B:
(Boat pattern - Still life)
0, 1
1, 0
2, 1
0, 2
1, 2
Output B:
0, 1
1, 0
2, 1
0, 2
1, 2
--------------------------------------------------------------------------------------------- ---------------------
Input C:
(Blinker pattern - oscillator)
1, 1
1, 0
1, 2
Output C:
1, 1
0, 1
2, 1
--------------------------------------------------------------------------------------------- ---------------------
Input D:
(Toad pattern - two phase oscillator)
1, 1
1, 2
1, 3
2, 2
2, 3
2, 4
Output D:
0, 2
1, 1
1, 4
2, 1
2, 4
3, 3
--------------------------------------------------------------------------------------------- ---------------------
