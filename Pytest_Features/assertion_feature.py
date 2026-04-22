import pytest


def test_compare1():
    assert 1 == 1 ,"condition 1 failed"
    assert 2 == 2, "condition 2 failed"


def test_compare2():
    assert 2 == 1 ,"condition 1 failed"
    assert 2 == 2, "condition 2 failed"

# nornal function will not be picked up by pytest
def compare3():
    assert 2 == 1 ,"condition 1 failed"
    assert 2 == 2, "condition 2 failed"