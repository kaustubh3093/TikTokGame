"""
Created on Sat Feb 15 22:51:08 2020
@author: Kaustubh
This is the code for Tik Tok game
"""

"""
Print the output in the board form to make it user friendly
"""
import random
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print (board[7] + '|' + board[8] + '|' + board[9])
    print (board[4] + '|' + board[5] + '|' + board[6])
    print (board[1] + '|' + board[2] + '|' + board[3])
    
"""Declared an board list of size 10 which has all empty space character initially"""
board = [' '] *10

"""
player_input method with except the marker argument which is either X or O based on the 
random selection of choose_first method. So if choose first return 0 marker is X otherwise 
it is O. It calls in loop for next player input and do all the necessary check:
    1) If player won after the input
    2) If all the space filled in the tik tok game then print the game is draw
"""
def player_input(marker):
    flag = False
    while(flag == False):
        move = player_choice(board)
        place_marker(board, marker, move)
        display_board(board)
        if win_check(board, 'X'):
            print("The player 1 has won the game")
            flag = True
        if win_check(board, 'O'):
            print("The player 2 has won the game")
            flag = True
        if full_board_check(board):
            print("The game between X and O is a draw")
            return False
        if marker == 'X':
            marker = 'O'
        elif marker == 'O':
            marker = 'X'
    return flag

"""
Will populate the list with the given marker at the defined position
"""
def place_marker(board, marker, position):
    board[position] = marker
    
"""
Perform operation for win condition:
    1) If any of the win condition satisfies it return true
    2) If non satisfies it return false
"""
def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    else:
        return False

"""
Return 0 and 1 based on the random function 
"""
def choose_first():
    num = random.randint(0,1)
    return num

"""
It will check if the given position is empty or it is filled
"""
def space_check(board, position):
    return board[position] == ' '

"""
It will return if all the board position is filled or not
"""
def full_board_check(board):
    full_board = board[1:]
    return ' ' not in full_board

"""
It performs the necessary check for player input:
    1) If input is not between 1-9 inclusive it will give message to the user
    2) If the input is already filled in the board it will ask for new input
"""
def player_choice(board):
    flag = False
    while flag == False:
        try:
            move = int(input('Enter the next move between 1-9 :'))
            if move < 1 or move > 9:
                print("Enter the correct value as input between 1-9")
                continue
            if space_check(board , move) == False:
                print("Enter the new input: This is already filled")
            else:
                flag = True
        except:
            print("Please insert an appropriate value between 0-9!")
    return move


"""
It will ask to user to input 1 to play again and for all other input code will terminate
"""
def replay():
    flag = True
    while flag == True:
        try:
            num = int(input('Enter 1 to play again :'))
            return num == 1
        except:
            print("Please insert an appropriate Number value!")


"""
Main block of the code:
    1) First take input from the choose_first method
    2) If it returns 1 then it calls player input method with marker O
    3) If it return 0 then it calls player input method with marker X
    4) Once the game is over it will call replay method 
    5) replay method will ask user whether play new game or not
"""
print('Welcome to Tic Tac Toe!')
while True:
    board = [' '] * 10
    turn = choose_first()
    if(turn == 1):
        print("Player 2 will start the game with market O")
        player_input('O')
    else:
        print("Player 1 will start the game with market X")
        player_input('X')
            
    print("The game is over")
    if(not replay()):
        break;
