import random
import copy

emptyTicTacToeBoard = {'top-L':' ','top-M':' ','top-R':' ',
                       'mid-L':' ','mid-M':' ','mid-R':' ',
                       'bom-L':' ','bom-M':' ','bom-R':' '}
def printTicTacToeBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['bom-L']+'|'+board['bom-M']+'|'+board['bom-R'])

def printMyTicTacToeBoard(board):
    print(board['q']+'|'+board['w']+'|'+board['e'])
    print('-+-+-')
    print(board['a']+'|'+board['s']+'|'+board['d'])
    print('-+-+-')
    print(board['z']+'|'+board['x']+'|'+board['c'])    

def fillUpTheBoard(listData):
    indexOfList = 0
    for k in emptyTicTacToeBoard.keys():
        #print(k+'_'+listData[indexOfList])
        emptyTicTacToeBoard[k]=listData[indexOfList]
        indexOfList+=1
                                           
printTicTacToeBoard(emptyTicTacToeBoard)
fillUpTheBoard(['O','X','O','X','O','X','O','X','O'])
printTicTacToeBoard(emptyTicTacToeBoard)

def inputSymbolOfYou():
    symbol = ''
    while not (symbol=='X' or symbol=='O'):
        print('Do you want to be X or O?')
        symbol = input().upper()

    if symbol=='X':
        return ['X','O']
    else:
        return ['O','X']

print(inputSymbolOfYou())

def getPlayerMove(board):
    move = ''
    while move not in ['q','w','e','a','s','d','z','x','c']:
        print('What is your next move?')
        move = input()
    return move

def whoGoesFirst():
 # Randomly choose the player who goes first.
      if random.randint(0, 1) == 0:
         return 'computer'
      else:
         return 'player'

def playAgain():
     # This function returns True if the player wants to play again, otherwise it returns False.
     print('Do you want to play again? (yes or no)')
     return input().lower().startswith('y')

def isWinner(bo,le):
    return  ((bo['q'] == le and bo['w'] == le and bo['e'] == le) or # across the top
      (bo['a'] == le and bo['s'] == le and bo['d'] == le) or # across the middle
      (bo['z'] == le and bo['x'] == le and bo['c'] == le) or # across the bottom
      (bo['q'] == le and bo['a'] == le and bo['z'] == le) or # down the left side
      (bo['w'] == le and bo['s'] == le and bo['x'] == le) or # down the middle
      (bo['e'] == le and bo['d'] == le and bo['c'] == le) or # down the right side
      (bo['q'] == le and bo['s'] == le and bo['c'] == le) or # diagonal
      (bo['e'] == le and bo['s'] == le and bo['z'] == le)) # diagonal

def isSpaceFree(board,move):
    return board[move]==' '
    
def isBoardFull(board):
    ' ' not in board.values()

def getBoardCopy(board):
    copyBoard = copy.copy(board)
    return copyBoard

def chooseRandomMoveFromList(board,moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) !=0:
        return random.choice(possibleMoves)
    else:
        return None
    
def getComputerMove(board,computerSymbol):
    if computerSymbol=='X':
       playerSymbol = 'O'
    else:
       playerSymbol='X'

    for i in board.keys():
        copyBoard = getBoardCopy(board)
        if isSpaceFree(copyBoard,i):
            copyBoard[i]=computerSymbol
            if isWinner(copyBoard,computerSymbol):
                return i

    for i in board.keys():
        copyBoard = getBoardCopy(board)
        if isSpaceFree(copyBoard,i):
            copyBoard[i] = playerSymbol
            if isWinner(copyBoard,playerSymbol):
                return i

    move = chooseRandomMoveFromList(board,['q','e','z','c'])
    if move!=None:
        return move
    return chooseRandomMoveFromList(board,['w','a','s','d','x'])
                        
    
print('Welcome to Tic Tac Toe!')
while True:
    ticTacToeBoard = {'q':' ','w':' ','e':' ',
                       'a':' ','s':' ','d':' ',
                       'z': ' ','x':' ','c':' '}
    playerSymbol, computerSymbol = inputSymbolOfYou()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn=='player':
            printMyTicTacToeBoard(ticTacToeBoard)
            move = getPlayerMove(ticTacToeBoard)
            ticTacToeBoard[move]=playerSymbol

            if isWinner(ticTacToeBoard,playerSymbol):
                printMyTicTacToeBoard(ticTacToeBoard)
                print('Ya ! You are the winner !')
                gameIsPlaying =False
            else:
                if isBoardFull(ticTacToeBoard):
                    printMyTicTacToeBoard(ticTacToeBoard)
                    print('Tie game !')
                    break
                else:
                    turn = 'computer'
        else:
            move = getComputerMove(ticTacToeBoard,computerSymbol)
            ticTacToeBoard[move]=computerSymbol

            if isWinner(ticTacToeBoard,computerSymbol):
                printMyTicTacToeBoard(ticTacToeBoard)
                print('No... ! You lose !') 
                gameIsPlaying =False
            else:
                if isBoardFull(ticTacToeBoard):
                    printMyTicTacToeBoard(ticTacToeBoard)
                    print('Tie game !')
                    break
                else:
                    turn = 'player'
    print('Play again ?(y or n)')
    if input().lower()=='n':
        break
                
