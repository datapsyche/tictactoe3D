'''
Board class for the game of TicTacToe.
Default board size is 3x3.
Board data:
  1=white(O), -1=black(X), 0=empty
  first dim is column , 2nd is row:
     pieces[0][0] is the top left square,
     pieces[2][0] is the bottom left square,
Squares are stored and manipulated as (x,y) tuples.

Author: Evgeny Tyurin, github.com/evg-tyurin
Date: Jan 5, 2018.

Based on the board for the game of Othello by Eric P. Nichols.

'''
# from bkcharts.attributes import color
import numpy as np

class Board():

    # list of all 8 directions on the board, as (x,y) offsets
    __directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]

    def __init__(self, n=3):
        "Set up initial board configuration."

        self.n = n
        # Create the empty board array.
        self.pieces = [None]*self.n
        for i in range(self.n):
            self.pieces[i] = [0]*self.n
            for j in range(self.n):
                self.pieces[i][j]=[0]*self.n
        # print(self[1],np.sum(self[1][1][:]))

    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black)
        @param color not used and came from previous version.        
        """
        moves = set()  # stores the legal moves.

        # Get all the empty squares (color==0)
        for x in range(self.n):
            for y in range(self.n):
                for z in range(self.n):
                    if self[x][y][z]==0:
                        newmove = (x,y,z)
                        moves.add(newmove)
        return list(moves)

    def has_legal_moves(self):
        for x in range(self.n):
            for y in range(self.n):
                for z in range(self.n):
                    if self[x][y][z]==0:
                        return True
        return False
    
    def is_win(self, color):
        """Check whether the given player has collected a triplet in any direction; 
        @param color (1=white,-1=black)
        # """
        results=[]
        for h in range(0,self.n):
            #check rows [h,i,: ]
            for i in range(0, self.n):
                results.append(np.sum(self[h][i][:]))
            # check columns [,: i]
            for i in range(0,self.n):
                results.append(np.sum(self[h][:][i]))
            # check the depth [,]
            for i in range(0,self.n):
                results.append(np.sum(self[:][h][i]))        
        
            # check the diagonals
            results.append(0)
            for i in range(0,self.n):
                results[-1] += self[h][i][i]
            results.append(0)
            for i in range(0,self.n):
                results[-1] += self[h][i][self.n-1-i]

        results.append(0)
        for i in range(0,self.n):
            results[-1] += self[i][i][i]
        results.append(0)
        for i in range(0,self.n):
            results[-1] += self[i][i][self.n-1-i]        

        for result in results:
            if abs(result) == self.n:
                return True

        return False

        # win = self.n
        # # check y-strips
        # for y in range(self.n):
        #     count = 0
        #     for x in range(self.n):
        #         if self[x][y]==color:
        #             count += 1
        #     if count==win:
        #         return True
        # # check x-strips
        # for x in range(self.n):
        #     count = 0
        #     for y in range(self.n):
        #         if self[x][y]==color:
        #             count += 1
        #     if count==win:
        #         return True
        # # check two diagonal strips
        # count = 0
        # for d in range(self.n):
        #     if self[d][d]==color:
        #         count += 1
        # if count==win:
        #     return True
        # count = 0
        # for d in range(self.n):
        #     if self[d][self.n-d-1]==color:
        #         count += 1
        # if count==win:
        #     return True
        
        # return False

    def execute_move(self, move, color):
        """Perform the given move on the board; 
        color gives the color pf the piece to play (1=white,-1=black)
        """

        (x,y,z) = move

        # Add the piece to the empty square.
        assert self[x][y][z] == 0
        self[x][y][z] = color


# if __name__=='__main__':
#     b1=Board(3)
