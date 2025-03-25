from Piece import Piece
from Constants import BLACK , WHITE , EMPTY_CELL
# from King import King
class Knight(Piece):
    def __init__(self,  color):
        super().__init__("Knight",color)

    def __str__(self):
        if(self.color == WHITE):
            return "N"
        else:
            return "n"

    def move(self,board,scoreboard,source,destination):
        if(self.is_valid_move(board.state,scoreboard, source, destination)==False):
            return False
        return super().move(scoreboard,board,source,destination)
        
            

    def is_valid_move(self,board,scoreboard,src,dest):
        if super().is_valid_move(board,scoreboard,src,dest) == False:
            return False
        row_diff = src[0]-dest[0] 
        col_diff = src[1]-dest[1]
        if (abs(row_diff) == 1 and  abs(col_diff) == 2) or ( abs(row_diff) == 2 and  abs(col_diff) == 1):
            return True
        else:
            return False    
        



