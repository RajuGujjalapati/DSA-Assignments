class Stack():
    def __init__(self):
        self.items = []#initializing empty list

    def push(self,item):#pushing variables into items list
        self.items.append(item)

    def pop(self):#getting the last element.
        return self.items.pop()

    def get_stack(self):#get_full stack(all stored variable)
        return self.items
    
    def is_empty(self):# is empty or not.#return True or False.
        return self.items == []
    
    def peek(self):#getting the last element.
        return self.items[-1]


s = Stack()
print(s.is_empty())
s.push("A")
s.push("B")
print(s.get_stack())
s.push("V")
print(s.get_stack())
print(s.pop())
print(s.get_stack())
print(s.peek())
