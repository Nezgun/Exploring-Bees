'''
Going to be used for bee's memory.  No need to edit the nodes as they come in, just dump them back into the hive
'''

from DataStorageSystems.Node import Node

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def insert(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1

    def insertAfter(self, target, data):
        newNode = Node(data, target.getLink())
        target.setLink(newNode)

    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.getData() == data:
                if current == self.head:
                    self.head = current.getLink()
                else:
                    previous.setLink(current.getLink())
                self.size -= 1
                return 1
            else:
                previous = current
                current = current.getLink()
        return 0

    def search(self, data):
        current = self.head
        while current:
            if current.getData() == data:
                return current
            else:
                current = current.getLink()
        return 0

    def getSize(self):
        return self.size

    def copy(self):
        return