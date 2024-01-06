import pytest

from utils.dicts import get_val

@pytest.fixture
def collection1_fixture():
    return {"vcs": "mercurial"}


@pytest.fixture
def collection2_fixture():
    return {}


def test1_get_val(collection1_fixture):
    assert get_val(collection1_fixture, "vcs") == 'mercurial'
    assert get_val(collection1_fixture, "vcs", "git") == 'mercurial'


def test2_get_val(collection2_fixture):
    assert get_val(collection2_fixture, "vcs") == 'git'
    assert get_val(collection2_fixture, "vcs", "bazaar") == "bazaar"

