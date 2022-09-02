
import chess

#################################################################
# ARGUMENTS:
# Dictionary with key value pairs that are used to get a response 
#################################################################


#################################################################
# PROBLEMI:
# Svako moguce pitanje i odgovor na pitanje moraju biti odredjeni
# unapred. 
#################################################################




# proverava se da li moze da se uradi rokada sa strane kralja
def castlingK(fen, args):
    if 'K' in fen.split(' ')[2]:
        return True
    else:
        return False

# proverava se da li moze da se uradi rokada sa strane kraljice
def castlingQ(fen, args):
    if 'Q' in fen.split(' ')[2]:
        return True
    else:
        return False

# proverava se da li je crni igrac napravio sah
def isCheck(fen, args):
    return chess.Board(fen=fen).is_check()

# proverava se da li je figura napadnuta i od strane kojeg tipa figura
def isAttacked(fen, args):
    return chess.Board(fen=fen).is_attacked_by(chess.BLACK, args['position'])

# proverava se da li figura napada neku drugu figuru
def isAttacking(fen, args):
    board = chess.Board(fen=fen)
    attacks = board.attacks(args['position'])
    board = f'{board}'.split()
    attacks = f'{attacks}'.split()
    for i in range(1, 64):
        if attacks[i] != '.' and board[i] != '.':
            return True
    return False

# proverava se da li je figura napravila sah
def madeCheck(fen, args):
    board = chess.Board(fen=fen)
    attacks = board.attacks(args['position'])
    board = f'{board}'.split()
    attacks = f'{attacks}'.split()
    for i in range(1, 64):
        if attacks[i] != '.' and board[i] == 'k':
            return True
    return False

# proverava se na kojem se figura polju nalazi
def position(fen, args):
    return args['position']



# proverava se da li figura brani kralja ili neku drugu figuru
# proverava se da li moze da se uradi en passant preko nekog polja
    # manje pametne/bitne ideje:
# proverava se na kom polju se nalaze kralj ili kraljica
# broji se razlika u poenima




print(isAttacked('8/8/8/8/8/8/8/R3q3 w - - 0 1', { 'position': chess.A1 }))



