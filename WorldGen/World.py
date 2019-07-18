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
        self.initializeFragrance()


    '''
    initializeFragrance: Cycles through all the tiles in the world and applies fragrance to them based on food locations
    args: none
    return:
        none
    Notes:
    1.  Cycles through all tiles on board
    2.  If tile contains food, generates a circle of radius where the minimum scent added is 1
    3.  Trims the circle's coordinates to fit the board.
    4.  Takes new list and adds fragrance at a rate of f(x) = fragrance / r^2
    '''
    def initializeFragrance(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j].isFoodSource():
                    fragrance = (self.board[i][j].getFragrance())
                    radius = round((10 * fragrance) ** 0.5)
                    origin = [i, j]
                    coordList = self.circleArea(origin, radius)
                    trimmedCoordList = self.coordinateFilter(coordList)
                    for entry in trimmedCoordList:
                        if entry == origin:
                            continue
                        dist = self.distance(entry, origin)
                        appliedFragrance = fragrance / (dist ** 2)
                        self.board[entry[0]][entry[1]].increaseFragrance(appliedFragrance)

    '''
    coordinateFilter: takes a list of coordinates, and filters out invalid ones based on board
    args: coordList
        coordList is a list of coordinates in [x, y] format.
    return:
        an updated list of coordinates with all out of bounds coordinates deleted.
    '''
    def coordinateFilter(self, coordList):
        maxX = self.size
        maxY = self.size
        trimmedList = []
        for entry in coordList:
            if entry[0] >= 0 and entry[0] < maxX and entry[1] >= 0 and entry[1] < maxY:
                trimmedList.append(entry)
        return trimmedList

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
    getBoardData: Returns a desired set of data from the board
    args: dataType
        dataType is the type of data that is desired from the board.
    return:
        Returns a list of coordinate pairs with the desired data.
    '''
    def getBoardData(self, dataType = "standard"):
        boardData = []
        for i in range(self.size):
            for j in range(self.size):
                coord = [i, j]
                if dataType == "fragrance":
                    data = self.board[i][j].getFragrance()
                elif dataType == "standard":
                    data = self.board[i][j].getFood()
                else:
                    print("Invalid dataType")
                entry = [coord, data]
                boardData.append(entry)
        return boardData

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
    distance: returns the distance between two coordinates
    args: coord1, coord2
        coord1 is the first pair of [x,y] coordinates
        coord2 is the second pair of [x,y] coordinates
    return:
        returns a double value that's the distance between the two points
    '''
    def distance(self, coord1, coord2):
        x1 = coord1[0]
        x2 = coord2[0]
        y1 = coord1[1]
        y2 = coord2[1]
        distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
        return distance

