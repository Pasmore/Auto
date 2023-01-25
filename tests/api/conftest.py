import pytest


@pytest.fixture(autouse=True)
def clean_test_file():
    with open("prodfile.txt", "w"):
        pass
