#WORLD GEN ISSUE: Takes up wayyyy too much ram for a 5k x 5k world.  Need to modularize the generation
#Generate a dictionary of coordinates that coorespond to their tiles, that way can iterate through a dictionary rather than a double for loop

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

    def getTile(self, x, y):
        return self.board[x][y]

    def gatherFood(self, coords):
        if self.board[coords[0]][coords[1]].isFoodSource():
            self.board[coords[0]][coords[1]].foodReduce()
            return 1
        else:
            return 0

    '''
    initializeFragrance: Cycles through all the tiles in the world and applies fragrance to them based on food locations
    args: none
    return:
        none
    '''
    def initializeFragrance(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].isFoodSource():
                    radius = (1/(self.board[i][j].getFrangrance()))**.5
                    origin = [i, j]
                    coordList = circleArea(origin, radius)
                    coordList = coordinateFilter(coordList)

    '''
    circleArea: generates a list of all the coordinates that fall within a circle of given radius/origin
    args: origin, radius
        origin is a coordinate pair in [x, y] format that marks the center of a circle
        radius is the radius of the circle
    return:
        a list of coordinates that fall within the area of a circle.  Does not account for world border.
    Notes:
        Circle Equation: (x-h)^2 + (y-k)^2 = r^2
        Knowns: y, h, k, r.  solve for x
        x^2 - 2xh + h^2 =r^2 - (y-k)^2 for (y=k to y=k+r)
        x^2 -2xh = r^2 - h^2 - (y-k)^2
    '''
    def circleArea(self, origin, radius):
        coordList = []
        h = origin[0]
        k = origin[1]
        constant = (radius ** 2) - (h ** 2)
        for y in range(k - radius, k + radius):
            for x in range(h - radius, h + radius):
                if ((x ** 2 - (2 * x * h)) - (constant - (y - k) ** 2)) <= 0.1:
                    coordList.append([x, y])
        return coordList

    '''
    coordinateFilter: takes a list of coordinates, and filters out invalid ones based on board
    args: coordList
        coordList is a list of coordinates in [x, y] format.
    return:
        an updated list of coordinates with all out of bounds coordinates deleted.
    '''
    def coordinateFilter(self, coordList):
        return

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


