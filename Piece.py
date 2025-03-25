from Constants import BLACK,WHITE,EMPTY_CELL
class Piece:
   
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def is_valid_move(self,board,scoreboard, src, dest):
        
    
        sourcePiece= board[src[0]][src[1]]
        destPiece = board[dest[0]][dest[1]]
        if( sourcePiece == EMPTY_CELL or self.is_turn_valid(sourcePiece.color, scoreboard.turn) == False):
            return False
        if destPiece != EMPTY_CELL and sourcePiece.color == destPiece.color:
            return False

    
    def is_turn_valid(self,color,turn):
        return color == turn
    def move(self,scoreboard,board,source,destination):
        destinationPiece = board.state[destination[0]][destination[1]]
        sourcePiece = board.state[source[0]][source[1]]
        board.state[destination[0]][destination[1]] = sourcePiece
        board.state[source[0]][source[1]]= EMPTY_CELL
        
        if sourcePiece.name == "King":
            if scoreboard.turn == WHITE:
                board.white_king_src = destination

            else:
                board.black_king_src = destination
        scoreboard.toggle_turn()

        if((self.color == WHITE and board.get_king(WHITE).is_check(board)) or (self.color == BLACK and board.get_king(BLACK).is_check(board))):
            board.state[source[0]][source[1]] = sourcePiece
            board.state[destination[0]][destination[1]] = destinationPiece
            scoreboard.toggle_turn()
            if sourcePiece.name == "King":
                if scoreboard.turn == WHITE:
                    board.white_king_src = source

                else:
                    board.black_king_src = source
            
            return False
        return True