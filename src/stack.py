class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        return self._data

    @property
    def next_node(self):
        return self._next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self._head = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self._head = Node(data, self._head)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """

        if self._head:
            data = self._head.data
            self._head = self._head.next_node
            return data
        return None

    @property
    def top(self) -> Node:
        return self._head
