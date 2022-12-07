from copy import deepcopy

from GameArea import GameArea
from Player import Player
from GameMode import isWinner
from move import move

# Checking if row can be complete by player or opponent
def evaluate(board : GameArea):

        if(isWinner(board,board.player_1)):
            return 10
        elif(isWinner(board,board.player_2)):
            return -10
        else:
            return 0

def allmovecirculartokens(board):
    tab = [[]]
    for col in range(3):
        for row in range(3):
            if (board.gamearea[row][col].squaretoken != None):
                if (board.gamearea[row][col].squaretoken.circletoken == None):
                    tab.append([row, col])
    tab.pop(0)

    return tab

def get_possible_moves(board,ismax):

    allmove= move()
    allmove.place_token=[[]]
    allmove.move_tokens=allmovecirculartokens(board)

    for col in range(3):
        for row in range(3):
             if(board.gamearea[row][col].squaretoken!=None):
                if(board.gamearea[row][col].squaretoken.circletoken==None):
                   allmove.place_token.append([row,col])
    allmove.place_token.pop(0)


    return allmove

def make_move(board,litlemove,indexmove,ismax):
    if(board==None):
        print("board is none")


    if(indexmove==0):
        if(ismax):
            board.addCircleToken(litlemove[0],litlemove[1],board.player_1)
            board.displayGameArea()
        else:
            board.addCircleToken(litlemove[0],litlemove[1],board.player_2)
            board.displayGameArea()







def minmax(state, depth, ismax):

   score = evaluate(state)
   if(score==10):
        return score
   if(score==-10):
        return score
   if(depth==0):
        return 0
   print("retour mini"+str(depth))

   listofmove =get_possible_moves(state, 1).place_token


   if ismax:
            bestValue = -5000
            for move in listofmove:
                print(listofmove)#le probleme est ici car la liste de move devient recursivement infinie
                state.displayGameArea()
                #copy du board
                newState = deepcopy(state)
                #on joue le coup
                make_move(newState, move, 0, 1)
                print("deeep="+str(depth)+"player 1"+str(move))
                value = minmax(newState, depth - 1, False)
                bestValue = max(bestValue, value)

            return bestValue

   else:
        bestValue = 5000
        for move in listofmove:
          print(listofmove)
          state.displayGameArea()
          #copy du board
          newState = deepcopy(state)
          #on joue le coup
          make_move(newState, move, 0, 0)
          print("deeep tour ="+str(depth)+"player 2"+str(move))
          value = minmax(newState, depth - 1, True)
          bestValue = min(bestValue, value)

        return bestValue

if __name__ == '__main__':
    player_1 = Player(0, "R")
    player_2 = Player(1, "B")
    board = GameArea(player_1, player_2)
    board.addCircleToken(2, 0, player_1)
    board.addCircleToken(2, 2, player_1)
    board.addCircleToken(1, 2, player_2)
    board.displayGameArea()
    print("la valeur maximal est "+str(minmax(board, 3,True)))










