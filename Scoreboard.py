from Constants import WHITE,BLACK
class Scoreboard:
    
    def __init__(self):
        
        self.turn = WHITE

    def toggle_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

