from src.stack import Node, Stack
import pytest


def test_node():
    n1 = Node(123, None)
    n2 = Node('123', n1)

    assert n2.next_node is n1
    assert n1.data == 123
    assert n2.data == '123'


def test_stack():
    stack = Stack()
    stack.push(1)
    stack.push('2')

    assert stack.top.data == '2'
    assert stack.pop() == '2'
    assert stack.pop() == 1
    assert stack.pop() is None
