from Validation import is_valid_move
from Constants import ARRAY_OF_ADDRESS,EMPTY_CELL
from Validation import toggle_turn


#  FUNCTION FOR MOVE
def move(board,source,destination):
 
    if(is_valid_move(board, source, destination)==False):
        return False



    temp = board [source[0]][source[1]]
    board[destination[0]][destination[1]] = temp
    board[source[0]][source[1]]= EMPTY_CELL

    toggle_turn()

