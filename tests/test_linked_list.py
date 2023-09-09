import pytest

from src.linked_list import LinkedList


@pytest.fixture
def linked_list_fixture():
    return LinkedList()


def test_linked_list_insert_beginning(linked_list_fixture):
    linked_list_fixture.insert_beginning({'id': 0})
    linked_list_fixture.insert_beginning({'id': 1})

    assert str(linked_list_fixture) == "{'id': 1} -> {'id': 0} -> None"


def test_linked_list_insert_at_end(linked_list_fixture):
    linked_list_fixture.insert_at_end({'id': 0})
    linked_list_fixture.insert_at_end({'id': 1})

    assert str(linked_list_fixture) == "{'id': 0} -> {'id': 1} -> None"


def test_linked_list_empty_str(linked_list_fixture):
    assert str(linked_list_fixture) == 'None'
