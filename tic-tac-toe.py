from line import Line
import time
import random

def print_board(board):
    """This function prints the board"""
    print(board[0] + " | " + board[1] + " | " + board[2] + "\n" + "---------" + "\n" +
        board[3] + " | " + board[4] + " | " + board[5] + "\n" + "---------" + "\n" +
        board[6] + " | " + board[7] + " | " + board[8])
    print("#######################") #prints a seperating line after the board
    
def print_ai_move(position):
    """This function prints out the AI's move"""
    print("The AI is thinking...")
    time.sleep(1.5)
    print("AI's move: " + str(position))

def player_turn(board, player, symbol):
    """This function takes in the current board and the player's requested move, checks if that position is availible and if so, 
    returns an updated version of the board where they have taken that position"""
    player_input = input(player + " move: ")    #asks for input
    updated_board = board.copy()    #copies the original board
    valid_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    #quit if the player types quit
    if player_input == "quit":    
        quit()

    #if the player doesn't enter a valid input run turn() again 
    elif player_input not in valid_positions:
        print("That isn't an option! Here are the numbers corresponding to valid positions: ")
        print("1" + " | " + "2" + " | " + "3" + "\n" + "---------" + "\n" +"4" + " | " + "5" + " | " + 
            "6" + "\n" + "---------" + "\n" + "7" + " | " + "8" + " | " + "9")
        return player_turn(board, player, symbol)   

    #if the position is taken run turn() again
    elif board[int(player_input) - 1] != " ": 
        print("That position is already taken! Try again.")
        return player_turn(board, player, symbol)   

    #otherwise, draw the player's symbol at the requested position and return the updated board
    else: 
        updated_board[int(player_input) - 1] = symbol
        return updated_board
            
def intelligent_move(board, lines):
    """This function makes a move for the AI"""
    updated_board = board.copy()

    for line in lines: 
        #if the AI can win this round, then draw O in the proper position to win
        if line.win_next_round("O") != False:
            print_ai_move(line.win_next_round("O"))
            updated_board[line.win_next_round("O")] = "O"
            return updated_board    #return here so if true the rest of the function doesn't run

        #elif the player can win next round, block them
        elif line.win_next_round("X") != False:
            print_ai_move(line.win_next_round("X"))
            updated_board[line.win_next_round("X")] = "O"
            return updated_board    #return here so if true the rest of the function doesn't run

    #if its open, take the center
    if board[4] == " ":
        print_ai_move(4)
        updated_board[4]  = "O"

    #elif its open, take a random corner
    elif board[0] == " " or board[2] == " " or board[6] == " " or board[8] == " ":
        availible_corners = []
        corners = [0, 2, 6, 8]

        for corner in corners:  #check if each corner is open and if so append it to te availible_corners list
            if board[corner] == " ":
                availible_corners.append(corner)
        
        move = random.choice(availible_corners) #pick a random corner from the list 
        print_ai_move(move)
        updated_board[move] = "O"

    #this should only happen if neither the AI or player are a move away from winning, the center is taken, and all corners are taken 
    #leaving only the center positions on each side (board[1], board[3], board[5], board[7])
    else: 
        availible_positions = []
        positions = [1, 3, 5, 7]
        for position in positions: #check if each position is open and if so append it to the availible_positions list
            if board[position] == " ":
                availible_positions.append(position)

        move = random.choice(availible_positions) #pick a random position from the list
        print_ai_move(move)
        updated_board[move] = "O"

    #return the updated board
    return updated_board
    
def random_move(board):
    """This function makes a move for the AI by randomly picking any availible position on the board"""
    updated_board = board.copy()
    availible_positions = []

    for position in range(9): #check if each position is open and if so append it to the availible_positions list 
        if board[position] == " ":
            availible_positions.append(position)

    move = random.choice(availible_positions)  #pick a random position from the list
    print_ai_move(move)
    updated_board[move] = "O"

    return updated_board

def play_again():
    """This function asks the player if they want to play again, if they say yes it returns true, otherwise it exits the program."""
    print("PLAY AGAIN?")
    answer = input("Yes or no: ").lower()

    while answer != "yes" and answer != "no" and answer != "quit":  #while the answer isn't yes, no, or quit ask for a new input
        answer = input("That isn't an option! Enter yes or no: ")   

    if answer == "yes": 
        return True
    else: 
        quit()

def single_player(difficulty):
    """This function runs the game in single player mode"""
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


    while continue_playing == True: #this loop repeats every turn
        #List of all possible orientations for 3 characters in a row (3 X's or O's)
        lines = [
            Line([board[0], 0], [board[1], 1], [board[2], 2]), #top
            Line([board[2], 2], [board[5], 5], [board[8], 8]), #right
            Line([board[6], 6], [board[7], 7], [board[8], 8]), #bottom
            Line([board[0], 0], [board[3], 3], [board[6], 6]), #left
            Line([board[1], 1], [board[4], 4], [board[7], 7]),   #center vertical 
            Line([board[3], 3], [board[4], 4], [board[5], 5]),  #center horizontal
            Line([board[2], 2], [board[4], 4], [board[6], 6]), #top right to bottom left
            Line([board[0], 0], [board[4], 4], [board[8], 8]) #top left to bottom right
        ]

        #number of possible win cases remaining for each player, starts at 8
        player_win_cases = 8   
        AI_win_cases = 8
        
        #Checks each line to see if anyone won or if its now impossible for one or both players to win along that line 
        for line in lines:  
            if line.win("X"):
                print("You won!")
                continue_playing = False

            elif line.win("O"):
                print("You lost.")
                continue_playing = False

            elif line.win_possible("X") == False:
                player_win_cases -= 1

            elif line.win_possible("O") == False:
                AI_win_cases -= 1

        #Detect if a win is impossible (cats game) and if so ends the game 
        if player_win_cases == 0 and AI_win_cases == 0 and continue_playing == True:
            print("Cat's game! No one wins.")
            continue_playing = False
            
        #if theres 1 space left on board and ((its the player's turn but a win is impossible for them) or 
        #(its the AI's turn but a win is impossible for them)) then its a cat's game
        elif board.count(" ") == 1 and ((turn_count % 2 == 0 and line.win_possible("X") == False) or 
        (turn_count % 2 == 1 and line.win_possible("O") == False)) and continue_playing == True:
            print("Cat's game! No one wins.")
            continue_playing = False        

        #if on an even numbered turn, its the player's move
        if turn_count % 2 == 0 and continue_playing == True: 
            this_turn = player_turn(board, "Your", "X")
            if this_turn == "quit":
                quit()
            else: 
                board = this_turn
                print_board(board)
                turn_count += 1

        #if on an odd numbered turn, its the AI's move
        elif continue_playing == True:
            if difficulty == "easy":    #if the difficulty is easy, then make a random move
                board = random_move(board)
                print_board(board)
                turn_count += 1

            elif difficulty == "medium":    #if the difficulty is medium, then theres a ~66% chance the AI will make an 
                random_float = random.random()  #intelligent move and a ~33% chance it will make a random move
                if random_float >= 0.66:
                    board = intelligent_move(board, lines)
                else:
                    board = random_move(board)
                
                print_board(board)
                turn_count += 1

            elif difficulty == "hard":  #if the difficulty is hard, then it will make an intelligent move every time
                board = intelligent_move(board, lines)
                print_board(board)
                turn_count += 1

def two_player():
    """This function runs the game in two player mode"""
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
        lines = [
            Line([board[0], 0], [board[1], 1], [board[2], 2]), #top
            Line([board[2], 2], [board[5], 5], [board[8], 8]), #right
            Line([board[6], 6], [board[7], 7], [board[8], 8]), #bottom
            Line([board[0], 0], [board[3], 3], [board[6], 6]), #left
            Line([board[1], 1], [board[4], 4], [board[7], 7]),   #center vertical 
            Line([board[3], 3], [board[4], 4], [board[5], 5]),  #center horizontal
            Line([board[2], 2], [board[4], 4], [board[6], 6]), #top right to bottom left
            Line([board[0], 0], [board[4], 4], [board[8], 8]) #top left to bottom right
        ]

        #number of possible win cases remaining for each player, starts at 8
        player1_win_cases = 8   
        player2_win_cases = 8
        
        #Checks each line to see if anyone won or if its now impossible for one or both players to win along that line 
        for line in lines:  
            if line.win("X"):
                print("Player1 won!")
                continue_playing = False

            elif line.win("O"):
                print("Player2 won!")
                continue_playing = False

            elif line.win_possible("X") == False:
                player1_win_cases -= 1

            elif line.win_possible("O") == False:
                player2_win_cases -= 1

        #Detect if a win is impossible (cats game) and if so end the game 
        if player1_win_cases == 0 and player2_win_cases == 0 and continue_playing == True:
            print("Cat's game! No one wins.")
            continue_playing = False
            
        #if 1 space left on board and ((its player1's turn but a win is impossible for them) or 
        #(its player2's turn but a win is impossible for them))
        elif board.count(" ") == 1 and ((turn_count % 2 == 0 and line.win_possible("X") == False) or 
        (turn_count % 2 == 1 and line.win_possible("O") == False)) and continue_playing == True:
            print("Cat's game! No one wins.")
            continue_playing = False
                
        #if on an even numbered turn, its player1's move 
        if turn_count % 2 == 0 and continue_playing == True: 
            this_turn = player_turn(board, "Player1's", "X")
            if this_turn == "quit":
                quit()
            else: 
                board = this_turn
                print_board(board)
                turn_count += 1

        #if on an odd numbered turn, its player2's move
        elif continue_playing == True:       
            this_turn = player_turn(board, "Player2's", "O")
            if this_turn == "quit":
                quit()
            else: 
                board = this_turn
                print_board(board)
                turn_count += 1

def main():
    """The main function has the player select the number of players and the game's mode"""
    print("SELECT NUMBER OF PLAYERS")
    num_of_players = input("1 or 2 players: ")
    
    #While the input isn't 1, 2, or quit, ask for a new input
    while num_of_players != "1" and num_of_players != "2" and num_of_players != "quit":
            print("That isn't an option! Enter 1 or 2")
            num_of_players = input("1 or 2 players: ")
    
    if num_of_players == "quit":
            quit()

    if num_of_players == "1":
        print("SELECT DIFFICULTY")
        difficulty = input("Enter easy, medium, or hard: ").lower()
        while difficulty != "easy" and difficulty != "medium" and difficulty != "hard" and difficulty != "quit":
            difficulty = input("That isn't an option! Enter easy, medium, or hard: ").lower() 
        
        if difficulty == "quit":
            quit()

        single_player(difficulty)

        if play_again() == True:    #run play_again() and if true, re-run main()
            main()
    else:
        two_player()

        if play_again() == True:    #run play_again() and if true, re-run main()
            main()
    
if __name__ == "__main__":
    main()