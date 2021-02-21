# fix the game. every time it tie
# Game board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

game_still_going = True

winner = None

current_player = "X"

# Display board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# Play a game pf tic tac toe
def play_game():
  
  # Display_inicial board
  display_board()

  # while game is till going 
  while game_still_going:
    
    # handle a single turn of an arbitrary player
    handle_turn(current_player)

    # check if the has ended
    check_if_game_over()
    
    # flip to the other player 
    flip_player()

  # the game has ended
  if winner == "X" or winner == "O":
    print("The winner is: " + winner)
  elif winner == None:
    print("Tie.")

# Handle a single turn of an arbitrary player
def handle_turn(player):

  print(player + "'s turn.")
  position = input("Choose a position from  1-9: ")

  valid = False
  while not valid:

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Invalid input. Choose a position from  1-9: ")

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:  
     print ("You may not go there! Go again.")
  

  board[position] = player

  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()

def check_for_winner():

  # set up global variables 
  global winner

  #Check rows
  row_winner = check_rows()
  #check columns
  column_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = diagonal_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return


def check_rows():
  # set up global variable
  global game_still_going
  # check if any of the rows have tha same value(and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  
  # if any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # return the winner (X or O);
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return


def check_columns():
  # set up global variable
  global game_still_going
  # check if any of the columns have tha same value(and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  #if any column does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # return the winner (X or O);
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return  


def check_diagonals():
  # set up global variable
  global game_still_going
  # check if any of the diagonals have tha same value(and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"
  #if any diagonal does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # return the winner (X or O);
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[6] 
  return



def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going =False
  return  


def flip_player():
  # global variable we need
  global current_player
  # if the current player was x, then change it ti O
  if current_player == "X":
    current_player = "O"
    #if the current player was O, then change it to X
  elif current_player == "O":
    current_player  = "X"
  return

play_game()
