import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from app import add_numbers, is_even

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False