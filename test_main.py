"""
Test goes here

"""

from main import func
import pandas as pd


def test_func():
    data = pd.read_csv("./data.csv")
    res = func(data)
    assert(len(res) == 0)


if __name__ == "__main__":
    test_func()
    print("CI passed.")