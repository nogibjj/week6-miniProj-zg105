"""
Test goes here

"""

from main import data_filter
import pandas as pd


def test_data_filter():
    dataframe = pd.read_csv("./data.csv")
    res = data_filter(dataframe)
    assert(len(res) == 0)


if __name__ == "__main__":
    test_data_filter()
    print("All tests passed.")