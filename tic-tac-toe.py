from line import Line

def print_board(board):
    """This function prints the board"""
    print(board[0] + " | " + board[1] + " | " + board[2] + "\n" + "---------" + "\n" +
                    board[3] + " | " + board[4] + " | " + board[5] + "\n" + "---------" + "\n" +
                    board[6] + " | " + board[7] + " | " + board[8])

def turn(board, player, symbol):
    """This function takes in the current board and the [player's requested move, checks if that position is availible and if so, 
    returns an updated version of the board where they have taken that position"""
    player_input = input(player + "'s move: ")
    updated_board = board.copy()    #copies the original board
    valid_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #quit if the player types quit
    if player_input == "quit":    
        return player_input

    #if the player doesn't enter a valid input run turn() again 
    elif player_input not in valid_positions:
        print("That isn't an option! Here are the numbers corresponding to valid positions: ")
        print("1" + " | " + "2" + " | " + "3" + "\n" + "---------" + "\n" +"4" + " | " + "5" + " | " + 
            "6" + "\n" + "---------" + "\n" + "7" + " | " + "8" + " | " + "9")
        return turn(board, player, symbol)

    #if the position is taken ask run turn() again
    elif board[int(player_input) - 1] != " ": 
        print("That position is already taken! Try again.")
        return turn(board, player, symbol)   #run the turn function again

    #otherwise, add the player's symbol 
    else: 
        updated_board[int(player_input) - 1] = symbol
        print_board(updated_board)
        return updated_board



#check is possible win function here
#for each line in possible win cases, if cats game then remove from list

def main():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


    continue_playing = True
    turn_count = 0
    #Starting instructions:
    print("To make a move, enter the number corresponding to the position of the box you want to put your mark in")
    print("1" + " | " + "2" + " | " + "3" + "\n" + "---------" + "\n" +
                    "4" + " | " + "5" + " | " + "6" + "\n" + "---------" + "\n" +
                    "7" + " | " + "8" + " | " + "9")
    print("Enter 'quit' to quit")
    #initial printing of board 
    print_board(board)

    while continue_playing == True:
        #List of all possible orientations for 3 characters in a row (3 X's or O's)
        lines = {
            "top" : Line(board[0], board[1], board[2]), 
            "right" : Line(board[2], board[5], board[8]),
            "bottom" : Line(board[6], board[7], board[8]),
            "left" : Line(board[0], board[3], board[6]),
            "vertical" : Line(board[1], board[4], board[7]),   #center vertical 
            "horizontal" : Line(board[3], board[4], board[5]),  #center horizontal
            "tr_2_bl" : Line(board[2], board[4], board[6]), #top right to bottom left
            "tl_2_br" : Line(board[0], board[4], board[8]), #top left to bottom right
        }
        #number of possible win cases remaining for each player, starts at 8
        player1_win_cases = 8   
        player2_win_cases = 8
        
        #Checks each line to see if anyone won or alternatively if its now impossible to win along that line and if 
        for line in lines:  
            if lines[line].win("X"):
                print("Player1 won!")
                continue_playing = False
    
            elif lines[line].win("O"):
                print("Player2 won!")
                continue_playing = False
            elif lines[line].win_possible("X") == False:
                player1_win_cases -= 1
            elif lines[line].win_possible("O") == False:
                player2_win_cases -= 1

        #Detect if a win is impossible (cats game) and if so end the game 
        if player1_win_cases == 0 and player2_win_cases == 0:
            print("Cat's game! No one wins.")
            continue_playing = False
        #if 1 space left on board and ((its player1's turn but a win is impossible for them) or 
        #(its player2's turn but a win is impossible for them))
        elif board.count(" ") == 1 and ((turn_count % 2 == 0 and lines[line].win_possible("X") == False) or 
        (turn_count % 2 == 1 and lines[line].win_possible("O") == False)):
            print("Cat's game! No one wins.")
            continue_playing = False
                
        #if on an even numbered turn, its player1's move 
        if turn_count % 2 == 0 and continue_playing == True: 
            this_turn = turn(board, "Player1", "X")
            if this_turn == "quit":
                continue_playing = False
            else: 
                board = this_turn

            turn_count += 1

        #if on an odd numbered turn, its player2's move
        elif continue_playing == True:       
            this_turn = turn(board, "Player2", "O")
            if this_turn == "quit":
                continue_playing = False
            else: 
                board = this_turn
            turn_count += 1

if __name__ == "__main__":
    main()