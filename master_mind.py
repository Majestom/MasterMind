from random import choice

# Dictionary containing all colours associated with letters. Gray is c for charcoal.
colours = {"r":"Red","y":"Yellow","b":"Blue","g":"Green","c":"Gray","p":"Purple","o":"Orange","w":"White"}

# Returns a random sub-set of five colours.
def generate_decoding_board_content():
    decoding_board_content = []
    i = 0
    for i in range(5):
        decoding_board_content.append(get_a_random_colour())
    return decoding_board_content

# Returns one random entry from the colours dictionary.
def get_a_random_colour():
    random_colour = choice(list(colours))
    return random_colour

# Create user board.
def create_user_board():
    user_board = [["","","","",""]]
    return user_board

def display_user_board(a_user_board):
    for e in a_user_board:
        print(e)

def add_to_user_board(user_board, user_input):
    request_user_input()
    new_guess_row = user_input.split(" ")
    print(new_guess_row)
    user_board.append(new_guess_row)
    return user_board

def request_user_input():
    print("Please enter a guess:")

def start():
    current_user_board = create_user_board()
    display_user_board()
    add_to_user_board()

# Display rules.

# Take input from user.

# Cleanse input to ensure it makes sense.

# Output key pegs for each input.
