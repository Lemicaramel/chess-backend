from Piece import Piece
from Constants import WHITE,EMPTY_CELL,BLACK
# from InitialState import initial_state
# from King import King
class Pawn(Piece):
    def __init__(self,  color):
        super().__init__("Pawn",color)

    def __str__(self):
        if(self.color == WHITE):
            return "P"
        else:
            return "p"

    def move(self,board,scoreboard,source,destination):
        if(self.is_valid_move(board.state,scoreboard, source, destination)==False):
            return False
        
        return super().move(scoreboard,board,source,destination)
            


    def is_valid_move(self,board,scoreboard,src,dest):
        if super().is_valid_move(board,scoreboard,src,dest) == False:
            return False
        row_diff = src[0]-dest[0] 
        col_diff = src[1]-dest[1]
        destPiece = board[dest[0]][dest[1]]
        if self.is_valid_pawn_move(destPiece, col_diff, scoreboard,row_diff,src,board):
            return True

        if self.pawn_capturing(destPiece,row_diff,col_diff,scoreboard):
            return True
        elif destPiece != EMPTY_CELL and abs(col_diff) == 1 and ((scoreboard.turn == WHITE and row_diff == 1) or (scoreboard.turn == BLACK and row_diff == -1)):
            return True
        else:
            return False 
        
        
    def is_valid_pawn_move(self,destPiece, col_diff, scoreboard,row_diff,src,board):
        isDestEmpty = destPiece == EMPTY_CELL
        isSameColumn = col_diff == 0
        isValidWhiteTurn = scoreboard.turn == WHITE and (row_diff == 1 or (src[0] == 6 and row_diff == 2 and board[src[0] - 1][src[1]] ==EMPTY_CELL))
        isValidBlackTurn = scoreboard.turn == BLACK and (row_diff == -1 or (src[0] == 1 and row_diff == -2 and board[src[0] + 1][src[1]] ==EMPTY_CELL))
        isValidPawnTurn = isValidBlackTurn or isValidWhiteTurn
        return isDestEmpty and isSameColumn and isValidPawnTurn


    def pawn_capturing(self ,destPiece,row_diff,col_diff,scoreboard):
       isDestEmpty = destPiece != EMPTY_CELL
       isDiagonalColumn = abs(col_diff) == 1
       isValidWhiteCapture= scoreboard.turn == WHITE and row_diff == 1
       isValidBlackCapture= scoreboard.turn == BLACK and row_diff == -1
       return isDestEmpty and isDiagonalColumn and isValidBlackCapture and isValidWhiteCapture
       

    def diagonal_capturing(self,board,scoreboard,src,dest):
        row_diff = src[0]-dest[0] 
        col_diff = src[1]-dest[1]
        destPiece = board[dest[0]][dest[1]]

        if( dest != EMPTY_CELL ) and ((scoreboard.turn == WHITE and destPiece == BLACK) or (scoreboard.turn == BLACK and destPiece == WHITE))and( col_diff == 1 and row_diff == 1):
           
            return True
        else: 
            return False


