from src.queue import Queue


def test_enqueue():
    queue1 = Queue()

    for i in range(4):
        queue1.enqueue(i)
        assert queue1.tail.data == i

    assert queue1.head.data == 0
    assert queue1.head.next_node.data == 1
    assert queue1.head.next_node.next_node.data == 2


def test_dequeue():
    queue1 = Queue()

    for i in range(4):
        queue1.enqueue(i)

    for i in range(4):
        assert queue1.dequeue() == i

    assert queue1.dequeue() is None

    assert queue1.head is None
    assert queue1.tail is None


def test_str():
    queue1 = Queue()

    assert str(queue1) == ""

    expected_result = ""
    for i in range(4):
        queue1.enqueue(i)
        expected_result += str(i) + '\n'

    assert str(queue1) == expected_result.rstrip()
