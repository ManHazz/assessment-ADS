class Stack:
  
    def __init__(self):
        self.items = []

    def push(self, student_name):
        self.items.append(student_name)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()  

    def is_empty(self):
        return len(self.items) == 0