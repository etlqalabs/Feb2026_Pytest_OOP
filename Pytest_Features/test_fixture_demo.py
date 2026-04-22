# read emp_src.csv file and run the count test

import pytest
import pandas as pd

@pytest.mark.order(4)
def test_count_check_1(read_file):
    print("test case 1 started....")
    expected_count = 3
    actual_count  = read_file.count()
    print("test case 1 finished....")

@pytest.mark.order(3)
def test_count_check_2(read_file):
    print("test case 2 started....")
    expected_count = 3
    actual_count  = read_file.count()
    print("test case 2 finished....")

@pytest.mark.order(2)
def test_count_check_3(read_file):
    print("test case 3 started....")
    expected_count = 3
    actual_count = read_file.count()
    print("test case 3 finished....")

@pytest.mark.order(1)
def test_count_check_4(read_file):
    print("test case 4 started....")
    expected_count = 3
    actual_count = read_file.count()
    print("test case 4 finished....")

