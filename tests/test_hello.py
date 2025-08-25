from app.hello import greet

def test_greet():
    assert greet("Luna") == "Hello, Luna!"
