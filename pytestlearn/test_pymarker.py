import pytest

@pytest.mark.functional
def test_login():
    print("Login test")

@pytest.mark.regression
def test_page():
    print("this is regression")