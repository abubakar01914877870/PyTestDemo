import pytest


@pytest.fixture(autouse=True)
def browser_setup():
    print("Create Driver")
    print("Launch Browser")

    yield
    print("Close Browser")
    print("Quite Driver")
