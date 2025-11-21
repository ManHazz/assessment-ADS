class Stack:
    """
    Baseline Structure: Stack (LIFO)
    Problem: Unfair processing (First person waits longest)
    """
    def __init__(self):
        self.items = []

    def push(self, student_name):
        self.items.append(student_name)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()  # Removes the LAST item added

    def is_empty(self):
        return len(self.items) == 0