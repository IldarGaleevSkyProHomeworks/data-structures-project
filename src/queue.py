class Node:
    """Класс для узла очереди"""

    def __init__(self, data):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self._tail = None
        self._head = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """

        new_node = Node(data)
        if self.tail:
            self.tail.next_node = new_node

        if self._head is None:
            self._head = new_node

        self._tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self._head:
            data = self._head.data
            self._head = self._head.next_node
            if self._head is None:
                self._tail = None
            return data
        return None

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def __str__(self):
        node = self._head
        result = ""
        while node:
            result += str(node.data)+'\n'
            node = node.next_node
        return result.rstrip()
