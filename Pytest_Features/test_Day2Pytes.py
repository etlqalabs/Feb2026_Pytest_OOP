# 1. Markers
# 2. Parllel execution
# 3. ordering tests
# 4. Re-running test cases
# 5. Exception handling

import pandas as pd

# Test Scenarios

# 1. Compare data between 2 files
import pytest
import os
import time

'''
# way 1 : without pytest assert method ( not recommonded)
def test_compare_src_and_tgt_bruteforce():
    df_src = pd.read_csv("Data/emp_src.csv")
    df_tgt = pd.read_csv("Data/emp_tgt.csv")
    if df_src.equals(df_tgt):
        print("Test Passed")
    else:
        print("Test Failed")
'''

# way 2 : with  pytest assert method (recommonded)
@pytest.mark.regression_tests
@pytest.mark.smoke_tests
def test_compare_src_and_tgt_using_assertion(source_data_setup,target_data_setup):
    assert source_data_setup.equals(target_data_setup),"Test case failed"

@pytest.mark.smoke_tests
def test_duplicate_check_src(source_data_setup):
    duplicate_count = source_data_setup.duplicated().sum()
    assert duplicate_count == 0, "there are duplicates in the source"

@pytest.mark.regression_tests
@pytest.mark.smoke_tests
def test_compare_src_and_tgt_using_assertion1(source_data_setup,target_data_setup):
    print(f"Executing test_compare_src_and_tgt_using_assertion1 in PID {os.getpid()}")
    time.sleep(3)
    assert source_data_setup.equals(target_data_setup),"Test case failed"

@pytest.mark.regression_tests
@pytest.mark.smoke_tests
def test_compare_src_and_tgt_using_assertion2(source_data_setup,target_data_setup):
    print(f"Executing test_compare_src_and_tgt_using_assertion2 in PID {os.getpid()}")
    time.sleep(3)
    assert source_data_setup.equals(target_data_setup),"Test case failed"

@pytest.mark.regression_tests
@pytest.mark.smoke_tests
def test_compare_src_and_tgt_using_assertion3(source_data_setup,target_data_setup):
    print(f"Executing test_compare_src_and_tgt_using_assertion3 in PID {os.getpid()}")
    time.sleep(3)
    assert source_data_setup.equals(target_data_setup),"Test case failed"

@pytest.mark.regression_tests
@pytest.mark.smoke_tests
def test_compare_src_and_tgt_using_assertion4(source_data_setup,target_data_setup):
    print(f"Executing test_compare_src_and_tgt_using_assertion4 in PID {os.getpid()}")
    time.sleep(3)
    assert source_data_setup.equals(target_data_setup),"Test case failed"

@pytest.mark.regression_tests
@pytest.mark.smoke_tests
def test_compare_src_and_tgt_using_assertion5(source_data_setup,target_data_setup):
    print(f"Executing test_compare_src_and_tgt_using_assertion5 in PID {os.getpid()}")
    time.sleep(3)
    assert source_data_setup.equals(target_data_setup),"Test case failed"

@pytest.mark.regression_tests
@pytest.mark.smoke_tests
def test_compare_src_and_tgt_using_assertion6(source_data_setup,target_data_setup):
    print(f"Executing test_compare_src_and_tgt_using_assertion6 in PID {os.getpid()}")
    time.sleep(3)
    assert source_data_setup.equals(target_data_setup),"Test case failed"



