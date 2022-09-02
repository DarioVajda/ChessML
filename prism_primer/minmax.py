import random
import chess


list = [ -1, 3, 5, -6, -4 ]
index = 0


def evaluate(position):

    if position.is_stalemate():
        print('DRAW')
        print(position)
        print()
        return 0
    
    if position.is_checkmate():
        print('LOSS')
        print(position)
        print()
        return -1000
    
    if chess.Board(flip_vertical(position)).is_checkmate():
        print('WIN')
        print(position)
        print()
        return 1000

    res = 0
    switch = {
        'Q': 9,
        'R': 5,
        'B': 3,
        'N': 3,
        'P': 1,
        'K': 0,

        'q': -9,
        'r': -5,
        'b': -3,
        'n': -3,
        'p': -1,
        'k': 0,
    }

    for piece in filter(lambda x: x != '.', f'{position}'.split()):
        # print(piece)
        res += switch[piece]

    print(res)
    print(position)
    print()
    # print()
    return res


#region flipping functions

def flip_colors(row):

    switch = {
        'Q': 'q',
        'R': 'r',
        'B': 'b',
        'N': 'n',
        'P': 'p',
        'K': 'k',

        'q': 'Q',
        'r': 'R',
        'b': 'B',
        'n': 'N',
        'p': 'P',
        'k': 'K',

        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
    }

    res = ''

    for i in range(0, len(row)):
        # print(switch[row[i]])
        res = res + switch[row[i]]


    return res

def flip_vertical(position):
    # print()
    rows = position.fen().split()[0].split('/')
    fen = ''
    for row in rows:
        fen = flip_colors(row) + '/' + fen
    return fen[:-1]

#endregion

def children(position, color=True):
    # true - white, false - black
    res = []


    if not color:
        position = chess.Board(fen=flip_vertical(position))
        # print(position)


    for move in position.legal_moves:
        # print(move)
        position.push(move)
        # print(flip_vertical(chess.Board(position)))
        # print(position.fen())
        fen = flip_vertical(chess.Board(fen=position.fen())) if not color else position.fen()
        res.append(chess.Board(fen=fen))
        position.pop()

    return res


def minimax(position, depth, maximizingPlayer, alpha=1e-8, beta=1e8):
    if depth == 0:
        res = evaluate(position)
        return [ res, 0 ]

    if maximizingPlayer:
        maxEval = -1e7
        childrenList = children(position, color=True)
        maxIndex = -1
        for child, index in zip(childrenList, range(0, len(childrenList))):
            [ eval, _ ] = minimax(child, depth - 1, False, alpha=alpha, beta=beta)
            if eval > maxEval:
                maxEval = eval
                maxIndex = index
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return [ maxEval, maxIndex ]
    else:
        minEval = 1e7
        childrenList = children(position, color=False)
        minIndex = -1
        for child, index in zip(childrenList, range(0, len(childrenList))):
            [ eval, _ ] = minimax(child, depth - 1, True, alpha=alpha, beta=beta)
            if eval < minEval:
                minEval = eval
                minIndex = index
            beta = min(beta, eval)
            if beta <= alpha:
                break
        if(minIndex) == -1: minEval = -100 # proveriti ko je pobedio
        return [ minEval, minIndex ]


# [res, move] = minimax(chess.Board('r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1'), 2, True)
# print(chess.Board('r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1'))
# print()

# [res, move] = minimax(chess.Board('r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1'), 3, True)
[res, move] = minimax(chess.Board('8/8/8/4p1K1/2k1P3/8/8/8'), 3, True)

print()
print(res, move)
print()

# position = chess.Board(fen='Qq6/8/8/8/8/8/8/8')
# position = chess.Board(fen='8/8/8/4p1K1/2k1P3/8/8/8')
# position = chess.Board(fen='r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1')

# print(chess.Board(fen='r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1'))
# print(chess.Board(fen=flip_vertical(chess.Board(fen='r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1'))))

# evaluate(position)
# childrenList = children(position, color=False)
# for child in childrenList:
#     print(child)
#     print()
#     pass
# print()