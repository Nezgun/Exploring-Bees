
from WorldGen.Tile import Tile

class World:
    
    def __init__(self, size = 100):
        self.size = size
        self.board = [[0] * size for i in range(size)]
        #i = x coord, j = y coord
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = Tile(i + 1, j + 1)

    def displayBoard(self):
        print(" " + ("_" * 3 * self.size))
        for i in range(self.size):
            display = "|"
            for j in range(self.size):
                display += str(self.board[i][j].getFood()).ljust(2) + " "
            display += "|"
            print(display)
        print("|" + ("_" * 3 * self.size) + "|")

