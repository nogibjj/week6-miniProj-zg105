"""
Test goes here

"""

import polars as pl

def test_data():
    data = pl.read_csv("data.csv")
    assert data.height > 0

if __name__ == "__main__":
    test_data()
    print("CI passed.")
