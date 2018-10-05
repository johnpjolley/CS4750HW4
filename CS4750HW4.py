from threading import Thread
import numpy as np
import time

#infinite = float("inf")
#negative_infinite = float("-inf")



def create_board(dimension):
    x = np.zeros(np.square(dimension), dtype=int)
    return x.reshape((dimension, dimension))

def choose(state, player):
    scoreCheck = 0
    for x in range(6):
        currentLine = -1
        nextLine = -1
        lineLength = 0
        next_lineLength = 0
        open_sides = 0
        lineEnds = False
        for y in range(6):
            currentLine = nextLine
            lineLength += next_lineLength
            next_lineLength = 0
            if state[x][y] != currentLine:
                if currentLine == -1:
                    lineLength = 1
                    nextLine = state[x][y]
                elif currentLine == 0:
                    open_sides += 1
                    lineLength = 1
                    nextLine = state[x][y]
                else:
                    lineEnds = True
                    if state[x][y] == 0:
                        open_sides += 1
                    else:
                        next_lineLength = 1
                    nextLine = state[x][y]
            else:
                if currentLine != 0:
                    lineLength += 1
            if y == 5:
                lineEnds = True
            if lineEnds:
                if lineLength == 1:
                    lineEnds = False
                    lineLength = 0
                    open_sides = 0
                else:
                    scoreCheck += score_line(currentLine, lineLength,
                                             open_sides, player)
                    lineEnds = False
                    lineLength = 0
                    open_sides = 0
    for y in range(6):
        currentLine = -1
        nextLine = -1
        lineLength = 0
        next_lineLength = 0
        open_sides = 0
        lineEnds = False
        for x in range(6):
            currentLine = nextLine
            lineLength += next_lineLength
            next_lineLength = 0
            if state[x][y] != currentLine:
                if currentLine == -1:
                    lineLength = 1
                    nextLine = state[x][y]
                elif currentLine == 0:
                    open_sides += 1
                    lineLength = 1
                    nextLine = state[x][y]
                else:
                    lineEnds = True
                    if state[x][y] == 0:
                        open_sides += 1
                    else:
                        next_lineLength = 1
                    nextLine = state[x][y]
            else:
                if currentLine != 0:
                    lineLength += 1
            if y == 5:
                lineEnds = True
            if lineEnds:
                if lineLength == 1:
                    lineEnds = False
                    lineLength = 0
                    open_sides = 0
                else:
                    scoreCheck += score_line(currentLine, lineLength,
                                             open_sides, player)
                    lineEnds = False
                    lineLength = 0
                    open_sides = 0
    for x_start in range(-3, 4, 1):
        x_offset = 0
        currentLine = -1
        nextLine = -1
        lineLength = 0
        next_lineLength = 0
        open_sides = 0
        lineEnds = False
        for y in range(6):
            x = x_start + x_offset
            if coordCheck(x, y):
                currentLine = nextLine
                lineLength += next_lineLength
                next_lineLength = 0
                if state[x][y] != currentLine:
                    if currentLine == -1:
                        lineLength = 1
                        nextLine = state[x][y]
                    elif currentLine == 0:
                        open_sides += 1
                        lineLength = 1
                        nextLine = state[x][y]
                    else:
                        lineEnds = True
                        if state[x][y] == 0:
                            open_sides += 1
                        else:
                            next_lineLength = 1
                        nextLine = state[x][y]
                else:
                    if currentLine != 0 and currentLine != -1:
                        lineLength += 1
                if y == 5:
                    lineEnds = True
                if lineEnds:
                    if lineLength == 1:
                        lineEnds = False
                        lineLength = 0
                        open_sides = 0
                    else:
                        scoreCheck += score_line(currentLine, lineLength,
                                                 open_sides, player)
                        lineEnds = False
                        lineLength = 0
                        open_sides = 0
            x_offset += 1
    for x_start in range(2, 8, 1):
        x_offset = 0
        currentLine = -1
        nextLine = -1
        lineLength = 0
        next_lineLength = 0
        open_sides = 0
        lineEnds = False
        for y in range(6):
            x = x_start + x_offset
            if coordCheck(x, y):
                currentLine = nextLine
                lineLength += next_lineLength
                next_lineLength = 0
                if state[x][y] != currentLine:
                    if currentLine == -1:
                        lineLength = 1
                        nextLine = state[x][y]
                    elif currentLine == 0:
                        open_sides += 1
                        lineLength = 1
                        nextLine = state[x][y]
                    else:
                        lineEnds = True
                        if state[x][y] == 0:
                            open_sides += 1
                        else:
                            next_lineLength = 1
                        nextLine = state[x][y]
                else:
                    if currentLine != 0 and currentLine != -1:
                        lineLength += 1
                if y == 5:
                    lineEnds = True
                if lineEnds:
                    if lineLength == 1:
                        lineEnds = False
                        lineLength = 0
                        open_sides = 0
                    else:
                        scoreCheck += score_line(currentLine, lineLength,
                                                 open_sides, player)
                        lineEnds = False
                        lineLength = 0
                        open_sides = 0
            x_offset -= 1
    return scoreCheck
def copy(board):
    return np.array(board)

def actionStateDecider(board, player):
    flag = 0
    for row in range(6):
        for col in range(6):
            if board[row][col] == 0:
                action = np.array([row, col])
                copiedBoard = copy(board)
                copiedBoard[row][col] = player
                state = copiedBoard
                if flag == 0:  
                    states = np.array([state])
                    actions = np.array([action])
                    flag = 1
                else:  
                    states = np.append(states, [state], axis=0)
                    actions = np.append(actions, [action], axis=0)
    if flag == 0:
        return np.array([]), np.array([])
    return actions, states



def fillPositions(state, player, max_depth, results, index):
    depth = 0
    results[index] = min_value(state, player, 9999999, -9999999, depth,max_depth)

def max_value(state, player, alpha, beta, depth, max_depth):
   
    newDepth = depth + 1
    
    if cutoff_test(state, depth, max_depth):
        return choose(state, player)
    v = -9999999
    a, s = actionStateDecider(state, player)
    for i in range(len(a)):
        v = max(v, min_value(s[i], player, alpha, beta, newDepth, max_depth))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def min_value(state, player, alpha, beta, depth, max_depth):

    newDepth = depth + 1
    
    alpha = 0 
    beta = 0 
    if cutoff_test(state, depth, max_depth):
        return choose(state, player)
    v = 9999999
    a, s = actionStateDecider(state, player)
    for i in range(len(a)):
        v = min(v, max_value(s[i], player, alpha, beta, newDepth, max_depth))
        if v >= alpha:
            return v
        beta = max(beta, v)
    return v


def checkMATE(state):
    result = choose(state, 1)
    if 5000 <= result or -5000 >= result:
        return True
    else:
        return False


def cutoff_test(state, depth, max_depth):
    if depth >= max_depth or checkMATE(state):
        return True
    else:
        return False

def ABprune(state, player, max_depth):
    actions, states = actionStateDecider(state, player)
    size = len(actions)
    board = copy(state)
    if size == 36:
        row = 2 + (np.random.random_integers(100) % 2)
        col = 2 + (np.random.random_integers(100) % 2)
        board = copy(state)
        board[row][col] = player
        #print(board)
        print("------")
        return board
    elif size == 0:
        print("tie!")
        return board
    threads = [None] * size
    results = np.zeros(size, dtype=int)
    for i in range(len(threads)):
        threads[i] = Thread(
            target=fillPositions, args=(states[i], player, max_depth, results, i))
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()
    print("||||||||||||||||||||||||||||")
    print("Player " + str(player))
    print(board)
    max = np.argmax(results)
    return states[max]

def score_line(currentLine, lineLength, open_sides, player):
    if lineLength == 4:
        if currentLine != player:
            return -999999
        else:
            return 999999
    if open_sides == 0:
        return 0
    else:
        if lineLength == 3:
            if open_sides == 2:
                if currentLine != player:
                    return -10
                else:
                    return 5
            elif open_sides == 1:
                if currentLine != player:
                    return -6
                else:
                    return 3
            else:
                exit("ERROR")
        elif lineLength == 2:
            if currentLine != player:
                return -1
            else:
                return 1
        else:
            return 0


def coordCheck(x, y):
    if x > 5:
        return False
    if x < 0:
        return False
    if y > 5:
        return False
    if y < 0:
        return False
    return True

def game():
        startTime0 = time.time()
        players = np.array([[1, 2], [2, 4]])

        turn = 0
        board = create_board(6)

        while not checkMATE(board):
            temptime1 = time.time()
            turn = turn % 2
            board = ABprune(board, players[turn][0], players[turn][1])
            turn = turn +1
            temptime2 = time.time()
            print("this turn took " + str(round(temptime2 - temptime1,4)) + "sec to finish")
        print('')
        print("End State:")
        print("##")
        print(board)
        whoWon = choose(board, players[0][0])
        elapsedTime0 = time.time() - startTime0

        if whoWon > 0:
            print('')
            print(' Results: ')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print("Player {0} wins!".format(players[0][0]))
            print("Time Elapsed: {:.3f} secs".format(elapsedTime0))
        else:
            print('')
            print(' Results:')
            print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
            print("Player {0} wins!".format(players[1][0]))
            print("Time Elapsed: {:.3f} secs".format(elapsedTime0))


game()
