import  pytest

def get_data():

    return [
        ("anand@isos.com","Summerr@2022"),
        ("vijay600@isos.com","Summerr@2022"),
        ("vijay00@isos.com", "Summerr@2022"),
    ]

@pytest.mark.parametrize("username,password",get_data())
def test_login(username,password):
    print(username, '---', password)