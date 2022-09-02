from loadData import Game
from moves import playGame, executeMove, whoseTurn
import chess
from copy import deepcopy

dataSetLines = open('dataset/all_with_filtered_anotations_since1998.txt', 'r')
loadStart = 0
loadEnd = 10000

# getting all the positions at which the white player had to make the decision and the moves the player made
i = 0
count = 0
for line in dataSetLines:
    i += 1
    if(i > loadEnd):
        break
    if(i < loadStart):
        continue

    game = Game(line)
    # print(game.result)
    if game.result == '1-0':
        count += 1
    positions = []
    board = chess.Board()
    for j in range(0, len(game.moves)):
        move = game.moves[j]
        board = executeMove(board, move)
        if board == False:
            positions.pop()
            break

        if j % 2 == 1 and j + 1 < len(game.moves):
            board = executeMove(board, game.moves[j+1])
            if board == False:
                positions.pop()
                break
            tempPiece = game.moves[j+1].split('.')[1][0]
            tempPiece = tempPiece if tempPiece in ['Q', 'K', 'B', 'N', 'R' ] else 'P'
            tempMove = f'{tempPiece}{board.pop()}'
            # print('tempMove', tempMove)
            positions.append([deepcopy(board), tempMove])
    
    print(i)
    for turn in positions:
        # print(f'{turn[1]}')
        with open(f'data/{turn[1]}.txt', 'a') as file:
            file.write(f'{turn}')
            file.write('\n')
        pass
    # print('\n')


print(count)