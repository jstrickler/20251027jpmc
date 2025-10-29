import sys
import pytest

@pytest.mark.skip(reason="dependencies not currently available")
def test_two_plus_two_equals_four():  # tests should begin with "test" (or will not be found automatically)
    assert 2 + 2 == 4   # if assert statement succeeds, the test passes

@pytest.mark.skipif(sys.platform != "win32", reason="Test only valid on Windows")
def test_success():
    assert True

@pytest.mark.xfail
def test_junk1():  #test expected to fail
    assert True

@pytest.mark.xfail
def test_junk2():  #test expected to fail
    assert False


if __name__ == "__main__":
    pytest.main([__file__, '-v'])