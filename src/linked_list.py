class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data: dict, next_node=None):
        self._data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data


class NodeIterator:
    def __init__(self, node: Node):
        self._curr_node = node

    def __next__(self):
        if self._curr_node:
            next_node = self._curr_node
            self._curr_node = next_node.next_node
            return next_node.data
        raise StopIteration


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self._first_element = None
        self._last_element = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data, self._first_element)
        self._first_element = new_node

        if self._last_element is None:
            self._last_element = new_node

    @property
    def head(self) -> Node:
        return self._first_element

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""

        # == for head-only way: ==
        #
        # curr_node = self._first_element
        # while curr_node:
        #     next_node = curr_node.next_node
        #     if next_node is None:
        #         next_node = Node(data)
        #         curr_node.next_node = next_node
        #         return
        #
        # self.insert_beginning(data)
        # ========================

        if self._last_element is None:
            self.insert_beginning(data)
            new_node = self._last_element
        else:
            new_node = Node(data)
        self._last_element.next_node = new_node
        self._last_element = new_node

    def to_list(self):
        return [node for node in self]

    def get_data_by_id(self, find_id):
        for node in self:
            try:
                if node["id"] == find_id:
                    return node
            except Exception as ex:
                # raise TypeError("Данные не являются словарем или в словаре нет id")
                print("Данные не являются словарем или в словаре нет id")
        return None

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def __iter__(self):
        return NodeIterator(self._first_element)
