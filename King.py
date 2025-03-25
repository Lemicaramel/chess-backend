from Piece import Piece
from Constants import WHITE,EMPTY_CELL,BLACK
class King(Piece):
    def __init__(self,  color):
        super().__init__("King",color)

    def __str__(self):
        if(self.color == WHITE):
            return "K"
        else:
            return "k"
        

    def move(self,board,scoreboard,source,destination):
        if(self.is_valid_move(board.state,scoreboard, source, destination)==False):
            return False
        
        return super().move(scoreboard,board,source,destination)

    def is_valid_move(self,board,scoreboard,src,dest):
        if super().is_valid_move(board,scoreboard,src,dest) == False:
            return False
        row_diff = src[0]-dest[0] 
        col_diff = src[1]-dest[1]
        if (col_diff == 1 or col_diff == -1 or  col_diff == 0) and  (row_diff == 1   or  row_diff == -1  or  row_diff == 0): 
            return True
        else:
            return False
        
    def is_check(self,board):
        return len(self.get_attackers(board)) > 0

    def checked_By_Knight(self,board):
        attackers = []
        king_pos = board.white_king_src if self.color == WHITE else board.black_king_src
        knight_moves = [
            (1, 2), (1, -2), (2, 1), (2, -1),
            (-1, 2), (-1, -2), (-2, 1), (-2, -1)
        ]
       
        for move in knight_moves:
            new_row = king_pos[0] + move[0]
            new_col = king_pos[1] + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board.state[new_row][new_col]
                if piece != EMPTY_CELL and piece.name == "Knight" and piece.color != self.color:
                   attackers.append((new_row, new_col)) 
                    
        return attackers
    
    def is_checked_with_Pawn(self,board):

        attackerCount = []
        king_pos = board.white_king_src if self.color == WHITE else board.black_king_src
        if self.color == WHITE:
            pawn_moves = [(-1, -1), (-1, 1)]  
        else:
            pawn_moves = [(1, -1), (1, 1)] 

        for move in pawn_moves:
            new_row = king_pos[0] + move[0]
            new_col = king_pos[1] + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board.state[new_row][new_col]
                if piece != EMPTY_CELL and piece.name == "Pawn" and piece.color != self.color:
                    attackerCount.append((new_row, new_col)) 
                    
        return attackerCount
    def is_checked_with_Bishop_or_Queen(self, board):
        attackers = []

        king_pos = board.white_king_src if self.color == WHITE else board.black_king_src

        bishop_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in bishop_directions:
            new_row = king_pos[0]+ direction[0]
            new_col = king_pos[1]+ direction[1]
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board.state[new_row][new_col]
                if piece != EMPTY_CELL:
                    if ( piece.name == "Bishop" or piece.name == "Queen")  and piece.color != self.color:     
                        attackers.append((new_row, new_col))
                    
                new_row += direction[0]
                new_col += direction[1]
                
        
        return attackers
    
    def is_checked_with_Rook_or_Queen(self,board):
        attackers = []
        king_pos = board.white_king_src if self.color == WHITE else board.black_king_src

        rook_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in rook_directions:
            new_row = king_pos[0]+ direction[0]
            new_col = king_pos[1]+ direction[1]
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board.state[new_row][new_col]
                if piece != EMPTY_CELL:
                    if (piece.name == "Rook" or piece.name == "Queen") and piece.color != self.color:
                        attackers.append((new_row, new_col))
                    
                new_row += direction[0]
                new_col += direction[1]

        return attackers
    

    def is_checkmate(self,scoreboard,board):
        if(self.is_check(board) == False):
            return False
        elif self.can_king_escape(scoreboard,board):
            return False
        elif len(self.get_attackers(board)) > 1:
            return True
        elif self.capture_attackers(board,scoreboard):
            return False

        return True
    
    def capture_attackers(self,board,scoreboard):
        attackers = self.get_attackers(board) 
        king_color = self.color
        can_capture = False
        king_pos = board.white_king_src if self.color == WHITE else board.black_king_src

   
        for row in range(8):
            for col in range(8):
                piece = board.state[row][col]

                if piece == EMPTY_CELL or piece.color != king_color:
                    continue

                for attacker_pos in attackers:
                    if piece.is_valid_move(board.state, scoreboard, (row, col),  attacker_pos): 
                        can_capture = True
                        break
                    # if self.block_attackers(piece,(row, col),king_pos,attacker_pos) == True:
                    #     return True
                        

        return can_capture

   


    def block_attackers(self,scoreboard,board,piece,piece_pos,king_pos,attacker_pos,):
        col_diff =(king_pos[1]-attacker_pos[1])
        row_diff = (king_pos[0]-attacker_pos[0])
    

        if king_pos[0] == attacker_pos[0]:
            direction = 1 if col_diff > 0 else -1
            for col in range(abs(king_pos[1]-attacker_pos[1])-1):
                blocking_pos = (king_pos[0], king_pos[1]+((col + 1 )*direction))
                if piece.is_valid_move(board.state, scoreboard, piece_pos,  blocking_pos):
                    return True
        if king_pos[1] == attacker_pos[1]:
            direction = 1 if row_diff > 0 else -1
            for row in range(abs(king_pos[0]-attacker_pos[0])-1):
                blocking_pos = ( king_pos[0]+((row + 1 )*direction),king_pos[1])
                if piece.is_valid_move(board.state, scoreboard, piece_pos,  blocking_pos):
                    return True
        if abs(king_pos[0]-attacker_pos[0]) == abs(king_pos[1]-attacker_pos[1]):

            print("Test C")
        return False
    def can_king_escape(self,scoreboard,board):
        
        can_escape = False
        king_pos = board.white_king_src if self.color == WHITE else board.black_king_src
        king_moves = [
                (1,1),(1,0),(1,-1),(0,-1),(0,1),(-1,1),(-1,0),(-1,-1)
        ]

        for moves in king_moves:
            destination_row = king_pos[0]+ moves[0]
            destination_column = king_pos[1]+ moves[1]
            if 0 > destination_row or destination_row > 7 or 0 > destination_column or destination_column > 7:
                continue
            destinationPiece = board.state[destination_row][destination_column]
            if destinationPiece != EMPTY_CELL and destinationPiece.color == self.color:
                continue
            sourcePiece = board.state[king_pos[0]][king_pos[1]]
            board.state[destination_row][destination_column] = sourcePiece
            board.state[king_pos[0]][king_pos[1]]= EMPTY_CELL
            if self.color == WHITE:
                board.white_king_src = [destination_row,destination_column]

            else:
                board.black_king_src =  [destination_row,destination_column]

            if self.is_check(board) == False:
                can_escape = True
                
            board.state[king_pos[0]][king_pos[1]] = sourcePiece
            board.state[destination_row][destination_column] = destinationPiece
            if self.color == WHITE:
                board.white_king_src = [king_pos[0], king_pos[1]]
            else:
                board.black_king_src = [king_pos[0], king_pos[1]]    
                
        return can_escape
    def get_attackers(self,board):
        attackers = []
        attackers += self.checked_By_Knight(board)
        attackers += self.is_checked_with_Pawn(board)
        attackers += self.is_checked_with_Bishop_or_Queen(board)
        attackers += self.is_checked_with_Rook_or_Queen(board)
        return  attackers
            