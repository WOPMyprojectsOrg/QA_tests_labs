"""Tests for max_of_three."""

import pytest

from tasks.task04 import max_of_three


@pytest.mark.parametrize(
    ("a", "b", "c", "expected"),
    [
        (1, 2, 3, 3),
        (10, -5, 7, 10),
        (-5, -2, -10, -2),
        (3, 3, 1, 3),
        (2.5, 2.7, 2.6, 2.7),
    ],
)
def test_max_of_three(a, b, c, expected):
    assert max_of_three(a, b, c) == expected
