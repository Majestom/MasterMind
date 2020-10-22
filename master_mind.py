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
    user_board = [["_","_","_","_","_"]]
    return user_board

# Adds a suitably formatted input string to the user_board.
def add_to_user_board(user_board, input_string):
    new_guess_row = input_string.split(" ")
    if user_board == [["_","_","_","_","_"]]:
        user_board[0] = new_guess_row
    else:
        user_board.append(new_guess_row)
    return user_board

# Prints user board.
def display_user_board(a_user_board):
    for e in a_user_board:
        print(e)

# Asks user for input.
def request_user_input():
    print("Please enter a guess:")
    return

# Checks that user input is valid.
def validate_user_input(input_string):
    new_guess_row = input_string.split(" ")

    if len(new_guess_row) != 5:
        print("You need to enter 5 distinct elements separated by spaces, not " + str(len(new_guess_row)) + ".")
        return "Invalid!"
    elif len(input_string) != 9:
        print("Input needs to be 9 characters long, not " + str(len(input_string)) + ".")
        return "Invalid!"
    else:
        e = ""
        for e in new_guess_row:
            if e not in colours.keys():
                print(e + " is not in set " + str(colours.keys()) + ".")
                return "Invalid!"
            elif len(e) != 1:
                print("Please enter individual characters separated by spaces.")
                return "Invalid!"
    return input_string

# Assigns answer pegs for user's guess.
def check_decoding_board_against_user_guess(decoding_board, current_user_board):
    black_answer_list = []
    white_answer_list = []
    position_of_colours_found = []
    i=0
    # Assign the black pegs.
    for i in range(len(decoding_board)):
        if decoding_board[i] == current_user_board[-1][i]:
            black_answer_list.append("black")
            position_of_colours_found.append(i)
    j=0
    k=0
    # Assign the white pegs.
    for j in range(len(decoding_board)):
        for k in range(len(current_user_board[-1])):
            if decoding_board[j] == current_user_board[-1][k] and k != j and j not in position_of_colours_found and k not in position_of_colours_found:
                white_answer_list.append("white")
                position_of_colours_found.append(j)
                position_of_colours_found.append(k)
    return black_answer_list, white_answer_list

def offer_hint(decoding_board_content):
    print("Hint: " + str(decoding_board_content))

def start():
    decoding_board_content = generate_decoding_board_content()
    current_user_board = create_user_board()
    user_input = ""
    while user_input != "q":
        display_user_board(current_user_board)
        request_user_input()
        user_input = input()
        if user_input == "q":
            break
        if user_input == "h":
            offer_hint(decoding_board_content)
        validated_user_input = validate_user_input(user_input)
        if validated_user_input != "Invalid!":
            current_user_board = add_to_user_board(current_user_board, validated_user_input)
            black_answer_list, white_answer_list = check_decoding_board_against_user_guess(decoding_board_content, current_user_board)
            if decoding_board_content == current_user_board[-1]:
                print(black_answer_list)
                print("You win!")
                break
            print(black_answer_list)
            print(white_answer_list)
        else:
            pass


start()
