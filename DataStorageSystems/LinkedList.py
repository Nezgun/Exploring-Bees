from DataStorageSystems.Node import Node

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def insert(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1

    def delete(self):
        return

    def search(self):
        return

    def getSize(self):
        return self.size
