import pytest
import pytest_check as check


def test_compare_hard_assert():
    assert 2 == 1, "condition 1 failed"
    print("hard - check 1")
    assert 2 == 2, "condition 2 failed"
    print("hard - check21")
    assert 3 == 3, "condition 3 failed"
    print("hard - check 2")

def test_compare_soft_assert():
    check.is_true(2 == 1,"condition 1 failed")
    print("soft - check 1")
    check.is_true(2 == 3, "condition 2 failed")
    print("soft - check 2")
    check.is_true(3 == 3, "condition 3 failed")
    print("soft - check 3")

