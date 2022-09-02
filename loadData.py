
def formatGameData(game):
    game = game.split()
    return [ game[2], game[17:] ]

class Game:
    def __init__(self, data):
        [ result, moves ] = formatGameData(data)
        self.result = result
        self.moves = moves

    def __repr__(self):
        return f'\nresult: {self.result}\nmoves:{self.moves}\n'

def load(start, end):
    lines = open('dataset/all_with_filtered_anotations_since1998.txt', 'r')
    
    data = []
    i = 0
    for line in lines:
        if(i >= end):
            break
        if(i >= start):
            data.append(Game(line))
        i += 1

    return data
