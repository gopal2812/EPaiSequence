import polygon
import poly_sequence
from polygon import *
from poly_sequence import *
from datetime import datetime
import pytest
from io import StringIO
import sys
import time
import inspect
import os
import re

README_CONTENT_CHECK_FOR = [
    'Polygon',
    'Poly_sequence',
    'max_efficiency',
]

def test_session10_readme_exists():
    """
    Method checks if there is a README.md file.
    failure_message: "README.md file missing!"
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_session10_readme_500_words():
    """
    Method checks if there are atleast 500 words in the README.md file
    failures_message: Make your README.md file interesting! Add atleast 500 words
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_session10_readme_proper_description():
    """
    Method checks if all the functions are described in the README.md file
    failures_message: You have not described all the functions/classes well in your README.md file
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session10_readme_file_for_more_than_10_hashes():
    """
    Method checks if README.md file has atleast 10 '#' (indentations)
    failures_message: You have not described all the functions/classes well in your README.md file
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 4


def test_polygon_indentations():
    """
    Method checks for proper indentations \
    Returns pass if used four spaces for each level of syntactically significant indenting.
    failures_message_1: Your script contains misplaced indentations
    failures_message_2: Your code indentation does not follow PEP8 guidelines
    """
    lines = inspect.getsource(Polygon)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_polygon_function_name_had_cap_letter():
    """
    Method checks for any Upper case in the function names in session10.py
    failures_message: You have used Capital letter(s) in your function names
    """
    functions = inspect.getmembers(Poly_sequence, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_poly_seq_function_name_had_cap_letter():
    """
    Method checks for any Upper case in the function names in session10.py
    failures_message: You have used Capital letter(s) in your function names
    """
    functions = inspect.getmembers(Poly_sequence, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_polygon_incorrect_params():
    try:
        Polygon(0, 0)
        assert False
    except IndexError:
        assert True


def test_polygon_param_types():
    p = Polygon(6, 2)
    abs_tol = 0.001
    rel_tol = 0.001
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)


def test_polygon_sequence_incorrect_param_types():
    try:
        output = Poly_sequence('10', 15)
        assert False
    except TypeError:
        assert True


def test_polygon_sequence_incorrect_params():
    try:
        output = Poly_sequence(10, 0)
        assert False
    except IndexError:
        assert True
