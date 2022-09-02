import chess

"""

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R

"""


def toTable(piece, x, y):
    str = ''
    for i in range(1, 9):
        if y != i:
            str += '8'
        else:
            if(x != 1):
                str += f'{x - 1}'
            str += piece
            if(x != 8):
                str += f'{8 - x}'
        str += '/'
    str = str[:-1]
    str += ' w - - 0 1'
    return str

def getListOfMoves(piece, legalMoves):
    list = []
    for move in legalMoves:
        list.append(f'{piece}{move}')
    return list

pieces = ['Q', 'K', 'B', 'N', 'R', 'P']
moveList = []
for piece in pieces:
    endy = 9
    if piece == 'P':
        endy = 8
    for x in range(1, 9):
        for y in range(1, endy):
            list = getListOfMoves(piece, chess.Board(fen=toTable(piece, x, y)).legal_moves)
            moveList = moveList + list

print(moveList)
print(len(moveList))
