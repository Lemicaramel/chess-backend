from Piece import Piece
from Constants import BLACK , WHITE , EMPTY_CELL
class Bishop(Piece):
    def __init__(self,  color):
        super().__init__("Bishop",color)

    def __str__(self):
        if(self.color == WHITE):
            return "B"
        else:
            return "b"
        
    def move(self,board,scoreboard,source,destination):
        if(self.is_valid_move(board.state,scoreboard, source, destination)==False):
            return False
        return super().move(scoreboard,board,source,destination)
            


    def is_valid_move(self,board,scoreboard,src,dest):
        if super().is_valid_move(board,scoreboard,src,dest) == False:
            return False
        row_diff = src[0]-dest[0] 
        col_diff = src[1]-dest[1]
    
        if row_diff == col_diff or row_diff == -col_diff:
           if self.is_piece_between(board,src,row_diff,col_diff) == True:
            return False

           
        else:
            return False

    def is_piece_between(self,board,src,row_diff,col_diff):
        for i in range(1,abs(row_diff)):
            if row_diff > 0:
                row_incr = -i
            else:
                row_incr = i
            if col_diff > 0:
                column_incr = -i
            else:
                column_incr = i
            if board[src[0] + row_incr][src[1] + column_incr] != EMPTY_CELL:
                return True
        return False
        