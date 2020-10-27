from random import choice

# Dictionary containing all colours associated with letters. Gray is c for charcoal.
colours = {"r":"Red","y":"Yellow","b":"Blue","g":"Green","c":"Gray","p":"Purple","o":"Orange","w":"White"}

# Dictionary containing ANSI escape sequences for various colours.
ansi_colours = {"r":"\033[91m","y":"\033[93m","b":"\033[34m","g":"\033[1;32m",\
"c":"\033[30m","p":"\033[35m","o":"\033[33m","w":"\033[37m"}

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
    new_guess_row = [char for char in input_string]
    if user_board == [["_","_","_","_","_"]]:
        user_board[0] = new_guess_row
    else:
        user_board.append(new_guess_row)
    return user_board

# Prints user board.
def display_user_board(a_user_board):
    for e in a_user_board:
        # print(e)
        colour_print(e)

# Asks user for input.
def request_user_input():
    print("Please enter a guess:")
    guess = input().lower().replace(" ", "")
    return guess

# Checks that user input is valid.
def validate_user_input(input_string):
    if len(input_string) != 5:
        print("You need to enter 5 distinct letters, not " + str(len(input_string)) + ".")
        return "Invalid!"
    # elif len(input_string) != 9:
    #     print("Input needs to be 9 characters long, not " + str(len(input_string)) + ".")
    #     return "Invalid!"
    else:
        e = ""
        for e in input_string:
            if e not in colours.keys():
                print(e + " is not in set " + str(colours.keys()) + ".")
                return "Invalid!"
            elif len(e) != 1:
                print("Please enter individual characters separated by spaces.")
                return "Invalid!"
    return input_string

# Assigns answer pegs for user's guess.
def check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board):
    black_answer_list = []
    white_answer_list = []

    new_a_decoding_board = []
    new_a_current_user_board = []

    i=0
    # Assign black pegs.
    for i in range(len(a_decoding_board)):
        if a_decoding_board[i] == a_current_user_board[-1][i]:
            black_answer_list.append("black")
        else:
            new_a_decoding_board.append(a_decoding_board[i])
            new_a_current_user_board.append(a_current_user_board[-1][i])

    # Assign white pegs.
    j=0
    k=0
    decoding_board_dict = dict()
    current_user_board_dict = dict()

    for e in new_a_decoding_board:
        decoding_board_dict[e] = 0
    for e in new_a_decoding_board:
        decoding_board_dict[e] = decoding_board_dict[e] + 1

    for e in new_a_current_user_board:
        current_user_board_dict[e] = 0
    for e in new_a_current_user_board:
        current_user_board_dict[e] = current_user_board_dict[e] + 1

    for key in decoding_board_dict:
        if key in current_user_board_dict:
            if decoding_board_dict[key] == current_user_board_dict[key]:
                i=0
                for i in range(decoding_board_dict[key]):
                    white_answer_list.append("white")
            elif decoding_board_dict[key] > current_user_board_dict[key]:
                i=0
                for i in range(current_user_board_dict[key]):
                    white_answer_list.append("white")
            elif decoding_board_dict[key] < current_user_board_dict[key]:
                i=0
                for i in range(decoding_board_dict[key]):
                    white_answer_list.append("white")

    return black_answer_list, white_answer_list

# By pressing "h" key the user can view the decoding board.
def offer_hint(decoding_board_content):
    print("Hint: " + str(decoding_board_content))

def colour_print(a_string):
    new_string = ""
    for c in a_string:
        if c in ansi_colours:
            new_string = new_string + ansi_colours[c] + c + "\033[00m"
        else:
            new_string = new_string + c
    print(new_string)

def start():
    decoding_board_content = generate_decoding_board_content()
    current_user_board = create_user_board()
    user_input = ""
    while user_input != "q":
        display_user_board(current_user_board)
        user_input = request_user_input()
        if user_input == "q":
            break
        if user_input == "h":
            offer_hint(decoding_board_content)
            validated_user_input = "Invalid!" # This means the layer skips a go.
        else:
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
