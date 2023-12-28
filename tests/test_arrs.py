import pytest

from utils.arrs import get, my_slice


@pytest.fixture # добавляю декоратор
def slice_fixture(): # фикстура
    return [1, 2, 3]


def test_get(slice_fixture):
    assert get(slice_fixture, 1, "test") == 2
    assert get([], 0, "test") == "test"


def test_my_slice(slice_fixture):
    assert my_slice([], 0, 0) == []
    assert my_slice(slice_fixture, None, 2) == [1, 2]
    assert my_slice(slice_fixture, 1, 2) == [2]
    assert my_slice(slice_fixture, 1) == [2, 3]
