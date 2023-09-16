import pytest
from io import StringIO

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


def test_linked_list_to_list(linked_list_fixture):
    test_data = [
        {'id': 0},
        {'id': 1}
    ]

    for data in test_data:
        linked_list_fixture.insert_at_end(data)

    assert linked_list_fixture.to_list() == test_data


def test_linked_list_get_data_by_id(linked_list_fixture):
    test_data = [
        {'id': 0, 'data': 'data_0'},
        {'id': 1, 'data': 'data_1'},
        {'id': 5, 'data': 'data_5'},
        {'id': 2, 'data': 'data_2'},
    ]

    for data in test_data:
        linked_list_fixture.insert_at_end(data)

    assert linked_list_fixture.get_data_by_id(0) == test_data[0]
    assert linked_list_fixture.get_data_by_id(5) == test_data[2]
    assert linked_list_fixture.get_data_by_id(2) == test_data[3]


def test_linked_list_get_data_by_id_raise_TypeError(linked_list_fixture, capsys):

    linked_list_fixture.insert_at_end(1)
    linked_list_fixture.insert_at_end("Data")
    linked_list_fixture.insert_at_end({'id': 1, 'data': 'data_0'})

    assert linked_list_fixture.get_data_by_id(1) == {'id': 1, 'data': 'data_0'}

    fake_print = capsys.readouterr()
    assert fake_print.out == 'Данные не являются словарем или в словаре нет id\n' * 2


