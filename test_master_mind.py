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
    # assert output.out == "\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\n\x1b[91mr\x1b[00m\n\x1b[91mr\x1b[00m\n\x1b[91mr\x1b[00m\n"
    assert output.out == "\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\n"
    # "\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\n"
    display_user_board([["r","r","r","r","r"],["y","y","y","y","y"]])
    output = capsys.readouterr()
    assert output.out == "\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\x1b[91mr\x1b[00m\n\x1b[93my\x1b[00m\x1b[93my\x1b[00m\x1b[93my\x1b[00m\x1b[93my\x1b[00m\x1b[93my\x1b[00m\n"

# def test_request_user_input(capsys):
#     request_user_input()
#     output = capsys.readouterr()
#     assert output.out == "Please enter a guess:\n"

def test_validate_user_input(capsys):
    assert validate_user_input("r") == "Invalid!"
    output = capsys.readouterr()
    assert output.out == "You need to enter 5 distinct letters, not 1.\n"
    assert validate_user_input("zzzzz") == "Invalid!"
    output = capsys.readouterr()
    assert output.out == "z is not in set dict_keys(['r', 'y', 'b', 'g', 'c', 'p', 'o', 'w']).\n"

def test_check_decoding_board_against_user_guess_01():
    a_decoding_board = ["r","r","r","r","r"]
    a_current_user_board = [["b","b","b","b","b"],["r","b","b","b","b"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == (["black"],[])

def test_check_decoding_board_against_user_guess_02():
    a_decoding_board = ["g","b","y","r","y"]
    a_current_user_board = [["b","b","b","b","b"],["y","w","w","w","w"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == ([],["white"])

def test_check_decoding_board_against_user_guess_03():
    a_decoding_board = ["r","b","b","b","b"]
    a_current_user_board = [["g","r","g","g","g"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == ([],["white"])

def test_check_decoding_board_against_user_guess_04():
    a_decoding_board = ["r","b","r","c","o"]
    a_current_user_board = [["r","r","g","g","g"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == (["black"],["white"])

def test_check_decoding_board_against_user_guess_05():
    a_decoding_board = ["r","c","w","r","o"]
    a_current_user_board = [["r","w","o","c","w"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == (["black"],["white","white","white"])

def test_check_decoding_board_against_user_guess_06():
    a_decoding_board = ["r","c","w","r","o"]
    a_current_user_board = [["r","r","c","o","r"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == (["black"],["white","white","white"])

def test_check_decoding_board_against_user_guess_07():
    a_decoding_board = ["r","c","w","r","o"]
    a_current_user_board = [["o","o","o","o","r"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == ([],["white","white"])

def test_check_decoding_board_against_user_guess_08():
    a_decoding_board = ["r","c","w","r","o"]
    a_current_user_board = [["r","o","o","o","o"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == (["black","black"],[])

def test_check_decoding_board_against_user_guess_09():
    a_decoding_board = ["r","c","w","r","o"]
    a_current_user_board = [["o","o","o","o","o"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == (["black"],[])

def test_check_decoding_board_against_user_guess_10():
    a_decoding_board = ["r","r","o","o","o"]
    a_current_user_board = [["w","w","w","r","r"]]
    assert check_decoding_board_against_user_guess(a_decoding_board, a_current_user_board) == ([],["white","white"])

def test_colour_print(capsys):
    colour_print("r")
    output = capsys.readouterr()
    assert output.out == "\033[91mr\033[00m\n"
