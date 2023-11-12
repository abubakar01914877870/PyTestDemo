import pytest

@pytest.fixture(autouse=True)
def shared_variable():
    data = {
        "BASE_URL": "https://rickandmortyapi.com/api"
    }
    return data
@pytest.fixture(autouse=True)
def browser_setup():
    print("Create Driver")
    print("Launch Browser")

    yield
    print("Close Browser")
    print("Quite Driver")
