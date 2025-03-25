from Constants import ARRAY_OF_ADDRESS,EMPTY_CELL

def coordinate(address):
    i = ARRAY_OF_ADDRESS.index(address[0])
    j = int(address[1])-1

    return (i,j)
def is_cell_empty(cell):
    return cell ==  EMPTY_CELL 


