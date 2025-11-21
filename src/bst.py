class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, item_data):
        if self.root is None:
            self.root = TreeNode(item_data)
        else:
            self._insert_recursive(self.root, item_data)

    def _insert_recursive(self, current_node, item_data):
        # Compare based on ID
        if item_data['id'] < current_node.data['id']:
            if current_node.left is None:
                current_node.left = TreeNode(item_data)
            else:
                self._insert_recursive(current_node.left, item_data)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(item_data)
            else:
                self._insert_recursive(current_node.right, item_data)

    def search(self, target_id):
    
        return self._search_recursive(self.root, target_id, 0)

    def _search_recursive(self, current_node, target_id, steps):
        steps += 1
        if current_node is None:
            return None, steps
        
        if target_id == current_node.data['id']:
            return current_node.data, steps
        elif target_id < current_node.data['id']:
            return self._search_recursive(current_node.left, target_id, steps)
        else:
            return self._search_recursive(current_node.right, target_id, steps)