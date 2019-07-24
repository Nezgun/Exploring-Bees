'''
Stack structure for building memory
'''

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        return

    #Standard
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[self.size]

    #Getters
    def getSize(self):
        return self.size