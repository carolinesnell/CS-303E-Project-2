
# File: Student.py
# Student: Caroline Snell
# UT EID: crs4775
# Course Name: CS303E
# 
# Date: October 12th 
# Description of Program: Tick-Tack-Toe
import random

HUMAN   = 0
MACHINE = 1
WELCOME = "Welcome to our Tic-Tac-Toe game!\nPlease begin playing."
YOU_WON  = "Congratulations! You won!\n"
YOU_LOST = "Sorry!  You lost!"
YOU_TIED = "Looks like a tie.  Better luck next time!"
    
def initialBoard():
    return  [ [" ", " ", " "], \
              [" ", " ", " "], \
              [" ", " ", " "] ]

class TicTacToe:


    def __init__(self):
        # Initialize the game with the board and current player
        self.player=HUMAN
        self.board=initialBoard()

    def __str__(self):
        s="\n"
        for i in range (0,len(self.board)): ##length of self.board gives you the number of rows
            for j in range(0, len(self.board[i])): ##length of a specific row gives you the number of clumns in that row 
                s=s+self.board[i][j]
                if (j<2):
                    s=s+"|"
            if i<2: 
                s=s+"\n-----\n"
        s = s+"\n"
        return s
            

    def getPlayer( self ):
        return(self.player)


    def isRowWin(self):
        for i in range(0,len(self.board)):
            if self.board[i][0]==self.board[i][1]==self.board[i][2] and self.board[i][0]!=" ":
                return True
        return False 
            
    def isColumnWin(self):
        for i in range(0,len(self.board)):
            if self.board[0][i]==self.board[1][i]==self.board[2][i] and self.board[0][i]!=" ":
                return True
        return False 

    def isDiagonalWin(self):
        if self.board[0][0]==self.board[1][1]==self.board[2][2] and self.board[0][0]!=" ":
            return True
        elif self.board[0][2]==self.board[1][1]==self.board[2][0] and self.board[0][2]!= " ":
            return True
        else:
            return False 


    def isWin( self ):
        return self.isRowWin() or self.isColumnWin() or self.isDiagonalWin()
        
    def swapPlayers( self ):
        if (self.player == HUMAN):
            self.player = MACHINE
        else:
            self.player = HUMAN
        
    def humanMove( self ):
        print("Your turn: ")
        valid = False
        
        while (valid == False):
            move = input("  Specify a move r, c: ")
            if (len(move) != 4 or move[1] != ','):
                print("\nResponse should be r, c. Try again!")
            else:
                r = int(move[0])
                c = int(move[3])

                if (r<0 or c<0 or r>2 or c>2):
                    print("\nIllegal move specified.  Try again!")
                elif (self.board[r][c] != " "):
                    print("\nIllegal move specified.  Try again!")
                else:
                    self.board[r][c] = "X"
                    valid = True
        
        # Ask the HUMAN to specify a move.  Check that it's 
        # valid (syntactically, in range, and the space is 
        # not occupied).  Update the board appropriately.

    def machineMove( self ):
        # This is the MACHINE's move.  It picks squares randomly
        # until it finds an empty one. Update the board appropriately.
        # Note: this is a really dumb way to play tic-tac-toe.  
        print("Machine's turn:")
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if self.board[r][c] == " ":
                print("  Machine chooses: ", r, ", ", c, sep="")
                self.board[r][c] = "O"
                return


def driver( ):
    """ This plays tic-tac-toe in a pretty simple-minded
    fashion.  The human player goes first with token "X" and
    alternates with the machine using token "O".  We print
    the board before the first move and after each move. """

    # Print the welcome message
    print( WELCOME )

    # Initialize the board and current player
    ttt = TicTacToe()
    print( ttt )

    # There are up to 9 moves in tic-tac-toe.
    for move in range(9):
        # The current player may be HUMAN
        # or MACHINE
        if ttt.getPlayer() == HUMAN:
            # If HUMAN, take a move, print the board,
            # and see if it's a win.
            ttt.humanMove()
            print( ttt )
            if ttt.isWin():
                print( YOU_WON )
                return

        else:
            # Else MACHINE takes a move.  Print the
            # board and see if the machine won.
            ttt.machineMove()
            print( ttt )
            if ttt.isWin():
                print( YOU_LOST )
                return

        # Swap players.
        ttt.swapPlayers()

    # After nine moves with no winner, it's a tie.
    print( YOU_TIED )
    
driver()

