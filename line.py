class Line:
    def __init__(self, a, b, c):
        """Init takes 3 lists as an argument, each list has 2 items, the first being the symbols and the second
        being the positions of said symbols"""
        #the symbols in the first, second, and third positions that make up the line
        self.s1 = a[0]
        self.s2 = b[0]
        self.s3 = c[0]

        #the positions of said symbols 
        self.p1 = a[1]
        self.p2 = b[1]
        self.p3 = c[1]

    def win(self, symbol):
        """This method checks if a player has won along this line and returns true or false"""
        if self.s1 == symbol and self.s2 == symbol and self.s3 == symbol:   #if all three positions in the line are 
            return True                                                     #the player's symbol then return true
        else:
            return False

    def win_possible(self, symbol):
        """This method checks if its still possible for a player to win along this line and returns true or false"""
        line_symbols = [self.s1, self.s2, self.s3]

        if symbol == "X":   #if the symbol is X then other (the other player's symbol) is O
            other = "O"
        else:               #else other is X
            other = "X"

        if other in line_symbols:   #if the other player's symbol is in that line, then return false
            return False   
        else:                       
            return True
    
    def win_next_round(self, symbol):
        """This method checks if the player is 1 move away from winning along this line and returns either the positon 
        that the player needs to take to win next round or false"""
        line_symbols = [self.s1, self.s2, self.s3] #possible symbols include "X", "O", or " "

        if line_symbols.count(symbol) == 2 and " " in line_symbols: #if there are 2 X's and 1 empty space in the line
            if self.s1 == " ": #if the blank is in the first position, return that position
                return self.p1 
            elif self.s2 == " ": #if the blank is in the second position, return that position
                return self.p2
            elif self.s3 == " ": #if the blank is in the third position, return that position
                return self.p3
        else: 
            return False



                
     

        

