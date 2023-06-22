import pytest

from app.calculations import add

# @pytest.mark.parametrize()
def test_add():
    print("testing add function")
    assert add(5,3) == 8
