class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        """Конструктор класса LinkedList"""
        self.head = self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next_node = self.head
            self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

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

    def to_list(self):
        """Возвращает список с данными"""
        ll_list = []
        node = self.head
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, data):
        """
        Возвращает первый найденный словарь с ключом 'id', значение которого равно переданному в метод значению.
        В случае возникновения TypeError выводится предупреждение и поиск продолжается
        """
        node = self.head
        while node:
            try:
                if node.data['id'] == data:
                    return node.data
            except TypeError:
                print('Данные не являются словарем или в словаре нет id')
            node = node.next_node
        return None
