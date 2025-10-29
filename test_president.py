import pytest
from president import President

@pytest.fixture
def potus():
    return President(29)

def test_one(potus):
    assert True