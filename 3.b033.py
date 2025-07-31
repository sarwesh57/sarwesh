class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top is None
    def push (self,data):
        new_node =Node(data)
        new_node.next=self.top
        self.top = new_node
    def pop (self):
        if self.is_empty():
            return None
        popped_data=self.top.data
        self.top=self.top.next
        return popped_data
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
stack=stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("peek:",stack.peek())
print("pop:",stack.pop())
print("pop:",stack.pop())
print("peek:",stack.peek())
print("is empty:",stack.is_empty())
