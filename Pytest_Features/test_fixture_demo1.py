# read emp_src.csv file and run the count test

import pytest
import pandas as pd

@pytest.mark.smoke_tests
@pytest.mark.regression_tests
def test_count_check(read_file):
    print("test case 1 started....")
    expected_count = 3
    actual_count  = read_file.count()
    print("test case 1 finished....")

@pytest.mark.skip
def test_duplicate_check(read_file):
    print("test case 2 started....")
    duplicate_count  = read_file.duplicated().sum()
    assert duplicate_count == 0,"there are duplicates in the file"
    print("test case 2 finished....")