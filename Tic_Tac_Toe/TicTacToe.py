'''
Created on September 14, 2021
Author: Brandon Hemminghaus
'''

'''
Check function checks the board to see if there is a winner
@param Board_list - Is the game board
@return - return true if there is a winner or false if no has won
'''
def CheckWinner(Board_list):
    #Checks the diagonals 
    if Board_list[0][0] == Board_list[1][1] == Board_list[2][2]:
        return True
    elif Board_list[0][2] == Board_list[1][1] == Board_list[2][0]:
        return True
    
    #Checks the rows
    for row in range(3):
        if Board_list[row][0] == Board_list[row][1] == Board_list[row][2]:
            return True

    #Checks the columns
    for column in range(3):
        if Board_list[0][column] == Board_list[1][column] == Board_list[2][column]:
            return True

'''
Check function checks the board to see if there is a draw
@param Board_list - Is the game board
@return - return true if there is a draw and false if not
'''
def CheckDraw(Board_list_Draw):
    count = 0
    for i in range(3):
        for j in range(3):
            if Board_list_Draw[i][j] == 'X' or Board_list_Draw[i][j] == 'O':
                count = count + 1
    if count == 9:
        return True
    return False

'''
This function draws the tictactoe board
@param B - Is the game board
'''
def DrawBoard(B):
    for i in range(3):
        for j in range(3):
            print(Board[i][j],end=" ")
        print("")

Board = [["1","2","3"],["4","5","6"],["7","8","9"]]
print("Welcome to Tic Tac Toe\nPlayer 1 is 'X'\nPlayer 2 is 'O'")
DrawBoard(Board)
Finished = False
Turn = True

while (Finished == False):
    move = input("Enter a number: ")
    for i in range(3):
        for j in range(3):
            if Board[i][j] == move and Turn == True:
                Board[i][j] = "X"
            if Board[i][j] == move and Turn == False:
                Board[i][j] = "O"
    
    DrawBoard(Board)
    if CheckWinner(Board):
        if Turn == True:
            print("Player 1 has won")
        else:
            print("Player 2 has won")
        Finished = True
    elif CheckDraw(Board):
        print("Draw, no winners")
        Finished = True
    Turn = not Turn