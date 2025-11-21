class Queue:
 
    def __init__(self):
        self.items = []

    def enqueue(self, student_name):
        self.items.append(student_name)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)  

    def is_empty(self):
        return len(self.items) == 0