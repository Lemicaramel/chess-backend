
from Scoreboard import Scoreboard
from Board import Board 
from Utility import coordinate,is_cell_empty
from Constants import WHITE,BLACK


def game():
    scoreboard = Scoreboard()









    board = Board()
    mistake = 0
    print("Turn for " +scoreboard.turn)
    board.print_board()
    gameStatus = True

    while gameStatus:
        srcInput = str(input("Enter your source move : "))
        if srcInput == "exit":
            return 
        destInput = str(input("Enter your dest move : "))
        source = coordinate(srcInput)
        destination = coordinate(destInput)
        piece = board.state[source[0]][source[1]]
        if is_cell_empty(piece):
            print("Watch Out! illegal Move.")
        else:
            if(piece.move(board,scoreboard,source,destination) == False):
                mistake += 1
                if(mistake > 1000):
                    print("Game Over")
                    return 
                print("Watch Out! illegal Move.")
        # board.get_king(WHITE).is_check(board)
        # board.get_king(BLACK).is_check(board)                
        print("--------------------------------")
        board.print_board()
        # if(board.get_king(WHITE) and board.get_king(WHITE).is_checkmate(scoreboard,board)):
        #     print("White is Checkmate, Black wins!!!")
        #     return
        # elif(board.get_king(BLACK) and board.get_king(BLACK).is_checkmate(scoreboard,board)):
        #     print("Black is Checkmate, White wins!!!")
        #     return
        print("Turn for " + scoreboard.turn)
        
        


game()
