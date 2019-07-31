
class Node:
    def __init__(self, data = None, link = None):
        self.data = data
        self.link = link

    def getData(self):
        return self.data

    def getLink(self):
        return self.link

    def setData(self, data):
        self.data = data

    def setLink(self, link):
        self.link = link

    def addNodeAfter(self, data):
        self.link = Node(data, self.link)

    def removeNodeAfter(self):
        self.link = self.link.getLink()