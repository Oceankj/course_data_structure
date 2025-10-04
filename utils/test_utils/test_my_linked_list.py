import pytest
from utils.my_linked_list import MyLinkedList, MyNode


@pytest.fixture
def ll():
    return MyLinkedList()


def test_initial_state(ll):
    assert ll.is_empty()
    assert ll.size() == 0


def test_add_last(ll):
    ll.add_last(10)
    assert not ll.is_empty()
    assert ll.size() == 1
    last_node = ll.get_last_node()
    assert last_node.value == 10


def test_add_multiple_nodes(ll):
    values = [1, 2, 3]
    for v in values:
        ll.add_last(v)
    assert ll.size() == 3
    last_node = ll.get_last_node()
    assert last_node.value == 3


def test_delete_node(ll):
    ll.add_last(5)
    node = ll.get_last_node()
    ll.delete_node(node)
    assert ll.is_empty()
    assert ll.size() == 0


def test_delete_node_multiple(ll):
    vals = [7, 8, 9]
    for v in vals:
        ll.add_last(v)
    node = ll.get_last_node()
    ll.delete_node(node)
    assert ll.size() == 2
    last_node = ll.get_last_node()
    assert last_node.value == 8


def test_add_before(ll):
    ll.add_last(1)
    ll.add_last(2)
    last_node = ll.get_last_node()
    new_node = MyNode(1.5)

    ll.add_before(last_node, new_node)
    assert ll.size() == 3

    assert last_node.prev.value == 1.5


def test_add_before_head_raises(ll):
    head = ll._MyLinkedList__head
    new_node = MyNode(99)
    with pytest.raises(ValueError):
        ll.add_before(head, new_node)


def test_delete_node_invalid(ll):
    node = MyNode(123)
    with pytest.raises(ValueError):
        ll.delete_node(node)


def test_get_last_node_empty(ll):
    with pytest.raises(ValueError):
        ll.get_last_node()
