import chess

# function executing the provided move on the provided board and returning the new version, the function returns false if something is wrong
def executeMove(board, move):
    moveSan = move.split('.')[1]
    try: 
        board.push_san(moveSan)
        return board
    except:
        return False

def playGame(moves=[]):
    board = chess.Board()
    # print(board.fen())
    for move in moves:
        board = executeMove(board, move)

def whoseTurn(move):
    return move[0] == 'W'

# playGame()