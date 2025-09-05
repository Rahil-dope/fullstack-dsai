# tests/test_exercises.py
from ..exercises import (
    formatted_sentence,
    sum_and_average,
    odd_numbers,
    mean,
    save_names,
    load_names,
)
import os

def test_formatted_sentence():
    assert "my age is 10" in formatted_sentence(10, 1.62, "HEllo")

def test_sum_and_avg():
    s, a = sum_and_average([1,2,3,4,5])
    assert s == 15
    assert a == 3.0

def test_odd_numbers():
    assert odd_numbers([1,2,3,4,5]) == [1,3,5]

def test_mean():
    assert mean([1,2,3,4]) == 2.5

def test_save_load_names(tmp_path):
    p = tmp_path / "names.txt"
    names = ["Alice","Bob","Charlie"]
    save_names(names, str(p))
    loaded = load_names(str(p))
    assert loaded == names
