from main import func

def test_func():
    # Test with a positive number
    result = func(0)
    assert result==1, "Test failed for the positive number"


if __name__ == "__main__":
    test_func()