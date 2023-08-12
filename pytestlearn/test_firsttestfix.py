import pytest
@pytest.fixture(scope='module')
def setup():
    print("Connect DB")
    yield
    print("close DB")
@pytest.fixture(scope='function')
def before():
    print("Launching the browser")
    yield
    print("Closing the browser")
"""
def test_firsttestcase(setup,before):
    print('Launching the first test case')

def test_secondtestcase(setup,before):
    print('Launching the second test case')
"""
@pytest.mark.usefixtures("setup","before")
def test_firsttestcase():
    print('Launching the first test case')

@pytest.mark.usefixtures("setup","before")
def test_secondtestcase():
    print('Launching the second test case')