#WORLD GEN ISSUE: Takes up wayyyy too much ram for a 5k x 5k world.  Need to modularize the generation

from WorldGen.Tile import Tile

class World:
    
    def __init__(self, size = 100):
        self.size = size
        self.board = [[0] * size for i in range(size)]
        #i = x coord, j = y coord
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j] = Tile(i + 1, j + 1)

    def getSize(self):
        return self.size

    def displayBoard(self):
        print(" " + ("_" * 3 * self.size))
        for i in range(self.size):
            display = "|"
            for j in range(self.size):
                display += str(self.board[i][j].getFood()).ljust(2) + " "
            display += "|"
            print(display)
        print("|" + ("_" * 3 * self.size) + "|")

    def displayCondensed(self):
        display = "   "
        for i in range(self.size):
            display += str(i).ljust(3)
        display += "\n"
        for i in range(self.size):
            display += str(i).ljust(3)
            for j in range(self.size):
                tileFood = self.board[i][j].getFood()
                if tileFood > 75:
                    display += "H".ljust(3)
                elif (tileFood <= 75 ) and (tileFood > 25):
                    display += "M".ljust(3)
                elif (tileFood <= 25) and (tileFood > 0):
                    display += "L".ljust(3)
                else:
                    display += " ".ljust(3)
            display += "\n"
        return display


