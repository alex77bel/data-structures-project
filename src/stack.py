class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data) -> None:
        """
        Метод для добавления элемента на вершину стека
        :param data: данные, которые будут добавлены на вершину стека
        """
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def pop(self):
        """
        Метод для вырезания элемента с вершины стека,
        возвращает этот элемент
        """
        if self.top is None:
            return None
        pop_result = self.top.data
        self.top = self.top.next_node
        return pop_result
