class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, item_data):
        """Inserts item at the beginning (O(1))"""
        new_node = Node(item_data)
        new_node.next = self.head
        self.head = new_node

    def linear_search(self, target_id):
        """
        Baseline Algorithm: Linear Search
        Time Complexity: O(n)
        """
        current = self.head
        steps = 0
        while current:
            steps += 1
            if current.data['id'] == target_id:
                return current.data, steps
            current = current.next
        return None, steps