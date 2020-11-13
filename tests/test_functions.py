import pytest

from project.functions import my_sum


def test_my_sum():
    assert my_sum(1, 2, 3, 4) == 10
 

def test_github_actions():
    assert False

