from Piece import Piece
from Constants import BLACK , WHITE , EMPTY_CELL
class Queen(Piece):
    def __init__(self,  color):
        super().__init__("Queen",color)

    def __str__(self):
        if(self.color == WHITE):
            return "Q"
        else:
            return "q"
        
    def move(self,board,scoreboard,source,destination):
        if(self.is_valid_move(board.state,scoreboard, source, destination)==False):
            return False
        return super().move(scoreboard,board,source,destination)
        
            


    def is_valid_move(self,board,scoreboard,src,dest):
        if super().is_valid_move(board,scoreboard,src,dest) == False:
            return False
        row_diff = src[0]-dest[0] 
        col_diff = src[1]-dest[1]
        if (row_diff == 0 or col_diff == 0) and self.is_piece_between_parallels(board,dest,src,row_diff,col_diff) == False:

            return True
        if(row_diff == col_diff or row_diff == -col_diff) and  self.is_piece_between_diagonal(board,src,row_diff,col_diff) == False:
            
            
            return True
        else:
            return False
    
    def is_piece_between_diagonal(self,board,src,row_diff,col_diff):
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
        

        
    def is_piece_between_parallels(self,board,dest,src,row_diff,col_diff):
        start = 0
        end = 0
        if row_diff == 0:
            if src[1] > dest[1]:
                start = dest[1]
                end = src[1]
            else:
                start = src[1]
                end = dest[1]
            for i in range(start+1,end):
                if board[src[0]][i] != EMPTY_CELL:
                    return True
            
            return False
        elif col_diff == 0:
            if src[0] > dest[0]:
                start = dest[0]
                end = src[0]
            else:
                start = src[0]
                end = dest[0]
            for i in range(start+1,end):
                if board[i][src[1]] != EMPTY_CELL:
                    return True
            
            return False
        else:
            return False