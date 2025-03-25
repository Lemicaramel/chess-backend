# FUNCTION FOR INITIALISATION OF PIECES
from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from King import King
from Constants import BLACK , WHITE , EMPTY_CELL

def initial_state():
    array2 = []
    for i in range(8):
        innerArray = []
        for j in range(8):
            innerArray.append(EMPTY_CELL)
        array2.append(innerArray)
    array2[7] = [Rook(WHITE),Knight(WHITE),Bishop(WHITE),Queen(WHITE),King(WHITE),Bishop(WHITE),Knight(WHITE),Rook(WHITE)]
    array2[0] = [Rook(BLACK),Knight(BLACK),Bishop(BLACK),Queen(BLACK),King(BLACK),Bishop(BLACK),Knight(BLACK),Rook(BLACK)]
    pawnWhiteArray = []
    pawnBlackArray = []
    
    for i in range(8):
        pawnWhiteArray.append(Pawn(WHITE))
        pawnBlackArray.append(Pawn(BLACK))
    array2[1] = pawnBlackArray 
    array2[6] = pawnWhiteArray 
    # array2[1] = ["P","P","P","P","P","P","P","P"]
    # array2[6] = ["p","p","p","p","p","p","p","p"] 
    return array2

