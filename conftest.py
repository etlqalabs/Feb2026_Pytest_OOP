import pandas as pd
import pytest

@pytest.fixture(scope='session')
def read_file():
    try:
        print("Before test execution step from fixture..")
        df = pd.read_csv("Data/emp_src1.csv")
    except FileNotFoundError as e:
        print(f"file doesn not exists -{e}")
    finally:
        yield df
        print("After test execution step from fixture..")


@pytest.fixture(scope='function',autouse=True)
def print_message():
    print("Before test execution step from fixture - print message..")
    yield
    print("After test execution step from fixture - print message..")


@pytest.fixture(scope='session')
def source_data_setup():
    df_src = pd.read_csv("Data/emp_src.csv")
    print("source file read - Before test exceution started")
    yield df_src
    print("After test exceution - source file")

@pytest.fixture(scope='session')
def target_data_setup():
    df_tgt = pd.read_csv("Data/emp_tgt.csv")
    print("Target file read - Before test exceution started")
    yield df_tgt
    print("After test exceution - traget file")

