# CS4750 - Artifical Intelligience
## HW4
### Randall Young
### John Jolley

Our implementation of the expanded tic-tac-toe game, with an AI that utilizes the min-max algorithm with the given heuristic (h(n)) is written in Python.

To begin running our program, type ``` python3 CS4750HW4.py ```
Sources used to aid in completion of this program include 

[MiniMax-Tic-Tac-Toe-implementation](https://codereview.stackexchange.com/questions/149363/minimax-tic-tac-toe-implementation)

[implementation of MiniMax using Higher Order Functions](http://www.giocc.com/concise-implementation-of-minimax-through-higher-order-functions.html)

During execution the time taken for each turn is given in the console, as well as the number of nodes generated.

## Runtime analysis

On an I7-4770 the game is complete in a near constant 2.3 seconds, never going past 2.7 but never completing in less than 2.