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

def add_to_user_board(user_board, input_string):
    new_guess_row = input_string.split(" ")
    # print(new_guess_row)
    if user_board == [["_","_","_","_","_"]]:
        user_board[0] = new_guess_row
    else:
        # user_board = user_board.append(new_guess_row)
        user_board.append(new_guess_row)
    # user_board.append(new_guess_row)
    return user_board

def display_user_board(a_user_board):
    for e in a_user_board:
        print(e)
    # print(a_user_board)

def request_user_input():
    print("Please enter a guess:")
    return
    # input_string = input()


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

def check_decoding_board_against_user_guess(decoding_board, current_user_board):
    answer_list = []
    i=0
    for i in range(len(decoding_board)):
        if decoding_board[i] == current_user_board[-1][i]:
            answer_list.append("black")
    return answer_list


def start():
    decoding_board_content = generate_decoding_board_content()
    current_user_board = create_user_board()
    user_input = ""
    while user_input != "q":
        display_user_board(current_user_board)
        print(decoding_board_content)
        request_user_input()
        user_input = input()
        if user_input == "q":
            break
        validated_user_input = validate_user_input(user_input)
        if validated_user_input != "Invalid!":
            current_user_board = add_to_user_board(current_user_board, validated_user_input)
        answer_list = check_decoding_board_against_user_guess(decoding_board_content, current_user_board[-1])
        # print("answer_list is " + str(answer_list))
        print(str(answer_list))
        print("current_user_board[-1] is " + str(current_user_board[-1]))
        if decoding_board_content == current_user_board[-1]:
            print("You win!")
            break
        print(answer_list)


# start()
