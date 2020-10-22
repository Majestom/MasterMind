from master_mind import *
import pytest

def test_get_a_random_colour():
    assert type(get_a_random_colour()) is str


def test_generate_decoding_board_content():
    assert len(generate_decoding_board_content()) == 5

def test_create_user_board():
    assert type(create_user_board()) is list
    assert len(create_user_board()) == 1
    assert len(create_user_board()[0]) == 5

def test_add_to_user_board():
    assert add_to_user_board([["r","r","r","r","r"]],"y y y y y") == [["r","r","r","r","r"],["y","y","y","y","y"]]

def test_display_user_board(capsys):
    assert type(display_user_board([["r","r","r","r","r"]])) is type(None)
    output = capsys.readouterr()
    assert output.out == "['r', 'r', 'r', 'r', 'r']\n"
    display_user_board([["r","r","r","r","r"],["y","y","y","y","y"]])
    output = capsys.readouterr()
    assert output.out == "['r', 'r', 'r', 'r', 'r']\n['y', 'y', 'y', 'y', 'y']\n"

def test_request_user_input(capsys):
    request_user_input()
    output = capsys.readouterr()
    assert output.out == "Please enter a guess:\n"

def test_validate_user_input(capsys):
    assert validate_user_input("r") == "Invalid!"
    output = capsys.readouterr()
    assert output.out == "You need to enter 5 distinct elements separated by spaces, not 1.\n"
    assert validate_user_input("ww w w w w") == "Invalid!"
    output = capsys.readouterr()
    assert output.out == "Input needs to be 9 characters long, not 10.\n"
    assert validate_user_input("z z z z z") == "Invalid!"
    output = capsys.readouterr()
    assert output.out == "z is not in set dict_keys(['r', 'y', 'b', 'g', 'c', 'p', 'o', 'w']).\n"

def test_check_decoding_board_against_user_guess():
    a_decoding_board = ["r","r","r","r","r"]
    a_current_user_board = [["b","b","b","b","b"],["r","b","b","b","b"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == (["black"],[])
    a_decoding_board = ["g","b","y","r","y"]
    a_current_user_board = [["b","b","b","b","b"],["y","w","w","w","w"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == ([],["white"])
    a_decoding_board = ["r","b","b","b","b"]
    a_current_user_board = [["g","r","g","g","g"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == ([],["white"])
    a_decoding_board = ["r","b","r","c","o"]
    a_current_user_board = [["r","r","g","g","g"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == (["black"],["white"])    
