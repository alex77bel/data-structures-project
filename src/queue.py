class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = self.tail = None

    def enqueue(self, data) -> None:
        """
        Метод для добавления элемента в очередь
        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        if self.head is None:  # пустая очередь
            self.head = self.tail = node
        else:  # непустая очередь
            self.tail.next_node = node
            self.tail = node

    def dequeue(self) -> str | None:
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        result = self.head.data
        self.head = self.head.next_node
        return result

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ''
        result = []
        index = self.head
        while index:
            result.append(index.data)
            index = index.next_node
        return '\n'.join(result)
