class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
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
        self.nodes = []

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека
        :param data: данные, которые будут добавлены на вершину стека
        """
        if self.nodes:
            self.nodes.append(Node(data, self.nodes[-1]))
        else:
            self.nodes.append(Node(data))

    def top(self):
        """
        Метод для возвращения элемента с вершины стека
        :return: данные элемента
        """
        if self.nodes:
            return self.nodes[-1]
        else:
            return None
