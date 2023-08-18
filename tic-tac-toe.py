import random

board = {
        "1": " ",
        "4": " ",
        "7": " ",
        "2": " ",
        "5": " ",
        "8": " ",
        "3": " ",
        "6": " ",
        "9": " ",
    }

available_squares = [
        "1",
        "4",
        "7",
        "2",
        "5",
        "8",
        "3",
        "6",
        "9",
    ]

def determine_winner(board):
    if board["1"] == board["4"] == board["7"] == "X" or board["1"] == board["4"] == board["7"] =="O":
        return board["1"]
    elif board["2"] == board["5"] == board["8"]== "X" or board["2"] == board["5"] == board["8"]== "O":
        return board["2"]
    elif board["3"] == board["6"] == board["9"] =="X" or board["3"] == board["6"] == board["9"] =="O":
        return board["3"]
    elif board["1"] == board["2"] == board["3"]=="X" or board["1"] == board["2"] == board["3"] =="O":
        return board["1"]
    elif board["4"] == board["5"] == board["6"] =="X" or board["4"] == board["5"] == board["6"] =="O":
        return board["4"]
    elif board["7"] == board["8"] == board["9"] =="X" or board["7"] == board["8"] == board["9"] =="O":
        return board["7"]
    elif board["1"] == board["5"] == board["9"] =="X" or board["1"] == board["5"] == board["9"] =="O":
        return board["1"]
    elif board["7"] == board["5"] == board["3"] =="X" or board["7"] == board["5"] == board["3"] =="O":
        return board["3"]
    else:
        return None
    

def print_board(board):
    print("-------------")
    print("|", board['1'], "|", board['2'], "|", board['3'], "|")
    print("|", board['4'], "|", board['5'], "|", board['6'], "|")
    print("|", board['7'], "|", board['8'], "|", board['9'], "|")
    print("-------------")

symbols = ["X", "O"]
flag=0
user_symbol = random.choice(symbols)
print("Your Choice is", user_symbol)
symbols.remove(user_symbol)

for i in range(8):
    print("Board is:")
    print_board(board)
    while(True):
        print("Your available choices are:", available_squares, "choose from them. (Note: Count starts from left to right)")
        user_choice = input()
        if user_choice not in available_squares:
            print("Choice Already Made/Unknown Choice, Retry")
        else:
            available_squares.remove(user_choice)
            board[user_choice]=user_symbol
            print("You chose", user_choice, "and the board is now:")
            print_board(board)
            break
    
    winner = determine_winner(board)
    if(winner!=None):
        print(f"Winner is {winner}!")
        flag=1
        break

    computer_choice = random.choice(list(available_squares))
    print("Computer Chose", computer_choice)
    board[computer_choice]=symbols[0]
    available_squares.remove(computer_choice)

    winner = determine_winner(board)
    if(winner!=None):
        print("Winner is:", winner)
        flag=1
        break

if flag==0:
    print("Draw Game!")
