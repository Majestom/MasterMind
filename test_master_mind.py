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
