"""
Test goes here

"""

import main
import polars as pl

def test_data():
    data = pl.read("data.csv")
    assert data.height > 0
    assert "grades" in data.columns

if __name__ == "__main__":
    test_data()
    print("CI passed.")
