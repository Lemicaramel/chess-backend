from termcolor import colored
from Constants import ARRAY_OF_ADDRESS,WHITE,BLACK
from InitialState import initial_state
class Board:
    def __init__(self):
        self.state = initial_state()
        self.black_king_src = (0,4)
        self.white_king_src = (7,4)

    def get_king(self,color):
        if color == WHITE:
            return self.state[self.white_king_src[0]][self.white_king_src[1]]
        else:
            return self.state[self.black_king_src[0]][self.black_king_src[1]]

    # FUNCTION FOR BOARD PRINTING
    def print_board(self):
        
        for num in range(8):
            position = num + 1
            print( "  " + str(position) , end = " ")
        print()
        print("-" * 32+"-")
        for i in range(8):
            print ( "|" , end = "")
            for j in range(8):
                cell_backround = "on_dark_grey"
                if (i+j)%2 == 0:
                    cell_backround = "on_white"
                temp = str(self.state[i][j])
                print(colored(" "+ temp + " ", "black",cell_backround)+"|" , end = "")
            print("    " + ARRAY_OF_ADDRESS[i] , end = "")
            print()
            print("-" * 32 +"-")


