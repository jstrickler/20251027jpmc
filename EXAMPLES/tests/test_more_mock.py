import pytest

def test_mocking(mocker):
    m = mocker.stub()
    m.get_data()  # call from subject under test
    m.get_data.assert_called()