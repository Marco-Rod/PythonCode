#! /usr/bin/python
class Stack:
    elements = []
    def __init__(self):
        self.elements = []

    def get_size(self):
        if len(self.elements)<=0:
            return "Longitud vacia"
        else:
            return len(self.elements)
    def push(self, x):
        self.elements.append(x)
    def pop(self):
        if len(self.elements)<=0:
            return "La lista esta vacia no puede utilizar el metodo pop"
        else:
            return self.elements.pop()
    def get_peek(self):
        return self.elements[-1]

    peek = property(fget=get_peek)
    size = property(fget=get_size)

s = Stack()
print(s.size)
print(s.pop())
# s.push("a")
# s.push("b")
# s.push("c")
# s.push("d")
# s.push("e")
# s.push("f")
# s.push("g")
# s.push("h")
#
# print(s.peek)
# print(s.size)
# print(s.elements)
# s.pop()
# print(s.elements)
# s.push("i")
# print(s.elements)
