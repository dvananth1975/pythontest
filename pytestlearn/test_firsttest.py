
def setup_module(module):
    print("Starting the Project with connection to DB")

def teardown_module(module):
    print("Closing the project")

def setup_function(function):
    print('Launching the browser')

def teardown_function(function):
    print('Quitting the browser')

def test_firsttestcase():
    print('Launching the first test case')

def test_secondtestcase():
    print('Launching the second test case')