from src.main import add

#just a tester for the add function from main.py module
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0