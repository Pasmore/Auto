import pytest
# from file1 import *


def division(a, b):
    return a/b


print(division(2, 3))


@pytest.mark.parametrize("a,b, expected_result", [(10, 2, 5),
                                                  (20, 10, 2),
                                                  (30, -3, -10)])
def test_division(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("expected_expection, divident, divider", [(ZeroDivisionError, 10, 0),
                                                                   (TypeError, 10, "2")])
def test_error_division(expected_expection, divident, divider):
    with pytest.raises(expected_expection):
        division(divident, divider)
