#https://codereview.stackexchange.com/questions/149363/minimax-tic-tac-toe-implementation
#http://www.giocc.com/concise-implementation-of-minimax-through-higher-order-functions.html
from operator import itemgetter

class GameState:
    def __init__(self,board):
        self.board = board

    #need function to determine if there is a winner
        
    def get_score(self,moves,turn): #implements the evaluation function on the game state and returns the h(n) value. Function is incomplete
        if len(moves) > 33: #determines if there are two or less pieces on board, no h(n) value in this case
            return 0 #may need to change
        xs = self.get_X_positions() #get positions on board of all the X's and put them in a list
        os = self.get_O_positions() #get positions on board of all the O's and put them in a list

    def break_tie(move, best_move): #if two positions have the same h(n) value, this determines which position to take
        priority = [14,15,20,21,7,8,9,10,13,16,19,22,25,26,27,28,0,1,2,3,4,5,6,11,12,17,18,23,24,29,30,31,32,33,34,35] #positions near middle get priority
        move_index = priority.index(move)
        best_move_index = priority.index(best_move)
        if move_index < best_move_index #determine which one is closer to the middle/higher priority
            return move_index
        else
            return best_move_index

    def get_X_positions(self): #find all positions on the board filled in with an 'X'
        xs = []
        for index, xs in enumerate(self.board):
            if xs == 'X':
                xs.append(index)
        return xs

    def get_O_positions(self): #find all positions on the board filled in with an 'O'
        os = []
        for index, os in enumerate(self.board):
            if os == 'X':
                os.append(index)
        return os

    def get_available_moves(self): #find all positions on the board  that have not been filled, have '_'
        squares = []
        for index, square in enumerate(self.board):
            if square != 'X' and square != 'O':
                squares.append(index)
        return squares

    def next_state(self,move,turn): #make the move at the position by placing the appropriate character in the move/position specified. Place 'X' if turn is 1 (for player 1) and 'O' if player 2 (turn should be 2)
        copy = self.board[:]
        copy[move] = 'X' if turn == 1 else 'O'
        return GameState(copy)

def minimax(game_state,player): #similar to the link, see it
        moves = game_state.get_available_moves()
        best_move = moves[0]
        best_score = float('-inf')
        for move in moves:
            clone = game_state.next_state(move, player)
            score = min_play(clone)
            score = get_score(clone)
            if score > best_score:
                best_move = move
                best_score = score
            elif score == best_score
                best_move = break_tie(move, best_move)
        return best_move, best_score

def min_play(game_state,player):
    if game_state.is_gameover():
        return evaluate(game_state)
    moves = game_state.get_available_moves()
    best_score = float('inf')
    for move in moves:
        clone = game_state.next_state(move, player)
        score = max_play(clone)
        score = get_score(clone)
        if score < best_score:
            best_move = move
            best_score = score
        elif score == best_score
                best_move = break_tie(move, best_move)
    return best_score

def max_play(game_state,player):
    if game_state.is_gameover():
        return evaluate(game_state)
    moves = game_state.get_available_moves()
    best_score = float('-inf')
    for move in moves:
        clone = game_state.next_state(move, player)
        score = min_play(clone)
        score = get_score(clone)
        if score > best_score:
            best_move = move
            best_score = score
        elif score == best_score
                best_move = break_tie(move, best_move)
    return best_score

start_game_state = GameState(['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'])

#go through back and forth in a while loop until there is a victor
move, heuristic = minimax(start_game_state, 1) #one call to minimax returns the move that has been made after the minimax simulation/run
move, heuristic = minimax(start_game_state, 2)

#minimax, min_play, and max_play need to be adjusted so that player 1 looks 2 moves deep and player 2 looks 4 moves deep
#need to print out the resulting Game State after each move is decided