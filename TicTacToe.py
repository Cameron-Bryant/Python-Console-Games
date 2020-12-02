import time
import random

dimensions = 3

class Board:
    def __init__(self):
        self.defaultValue = ' '
        self.board = [[self.defaultValue] * dimensions for i in range(dimensions)]
    def printBoard(self):
        for i in range(len(self.board)):
            print("\t" + str(self.board[i]))
        print('\n\n\n\n\n')

    def resetBoard(self):
        self.board = [[self.defaultValue] * dimensions for i in range(dimensions)]

    def updateBoard(self, x, y, val):
        self.board[y][x] = val

    def checkForWin(self):
        if self.board[1][1] == 'X':
            if self.board[1][2] == 'X' and self.board[1][0] == 'X':
                return True
            elif self.board[2][1] == 'X' and self.board[0][1] == 'X':
                return True
            elif self.board[0][0] == 'X' and self.board[2][2] == 'X':
                return True
            elif self.board[2][0] == 'X' and self.board[0][2] == 'X':
                return True
            else:
                return False
        elif self.board[1][1] == 'O':
            if self.board[1][2] == 'O' and self.board[1][0] == 'O':
                return True
            elif self.board[2][1] == 'O' and self.board[0][1] == 'O':
                return True
            elif self.board[0][0] == 'O' and self.board[2][2] == 'O':
                return True
            elif self.board[2][0] == 'O' and self.board[0][2] == 'O':
                return True
            else:
                return False
        else:
            return False

b = Board()

class Player:
    def __init__(self, disp):
        self.dispChar = disp

    def placePiece(self, coords):
        if  b.board[coords[1]][coords[0]] == ' ':
            b.board[coords[1]][coords[0]] = self.dispChar
        
playerX = Player('X')
playerO = Player('O')
b.printBoard()

def playTicTacToe():
    while True:
        inp = input("X:>")
        p = [int(inp.split()[0]), int(inp.split()[1])]
        if p[0] < 3 and p[1] < 3:
            playerX.placePiece(p)
        b.printBoard()
        if b.checkForWin() == True:
            print("X won! Play Again!")
            b.resetBoard()
        inp = input("O:>")
        p = [int(inp.split()[0]), int(inp.split()[1])]
        if p[0] < 3 and p[1] < 3:
            playerO.placePiece(p)
        b.printBoard()
        if b.checkForWin() == True:
            print("O won! Play Again!")
            b.resetBoard()

playTicTacToe()
