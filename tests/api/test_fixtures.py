
import pytest


@pytest.mark.check
def test_change_name(user):
    assert user.name == "Dmitry"


@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == "Pasmore"
