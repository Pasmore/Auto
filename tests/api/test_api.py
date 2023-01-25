import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ""
    assert user.name == ""


@pytest.mark.check
def test_name(user):
    assert user.name == "Dmitry"


@pytest.mark.check
def tets_second_name(user):
    assert user.second_name == "Pasmore"
