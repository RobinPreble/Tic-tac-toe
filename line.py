class Line:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def __str__(self):
        return f"<{self.p1}, {self.p2}, {self.p3}>"

    def win(self, symbol):
        if self.p1 == symbol and self.p2 == symbol and self.p3 == symbol:
            return True
        else:
            return False

    def win_possible(self, symbol):
        positions = [self.p1, self.p2, self.p3]

        if symbol == "X":
            other = "O"
        else: 
            other = "X"

        if other in positions:
            return False
        else:
            return True
        
        #if a win isn't possible in this line, return true

