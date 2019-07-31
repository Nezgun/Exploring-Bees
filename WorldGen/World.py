# -*- coding: utf-8 -*-

#WORLD GEN ISSUE: Takes up wayyyy too much ram for a 5k x 5k world.  Need to modularize the generation
import random

from WorldGen.Tile import Tile

class World:
    
    def __init__(self, size = 100, hives = 1):
        #Setup Frame
        self._size = size
        self.board = []

        self.numHives = hives
        self.hiveLocations = []

        self.foodLocations = []

        #Initialize Data
        self.initializeBoard()
        self.initializeFragrance()
        self.initializeHives()


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
        for tile in self.board:
            if tile.isFoodSource():
                self.foodLocations.append(self.indexToCoordinate(self.board.index(tile))) #adds to food source list
                fragrance = tile.getFragrance()
                radius = round((10 * fragrance) ** 0.5)
                origin = self.indexToCoordinate(self.board.index(tile))
                coordList = self.coordinateFilter(self.circleArea(origin, radius))
                for entry in coordList:
                    if entry == origin:
                        appliedFragrance = fragrance
                        continue
                    dist = self.distance(entry, origin)
                    appliedFragrance = fragrance / (dist ** 2)
                    index = self.coordinateToIndex(entry)
                    tileSelection = self.board[index]
                    tileSelection.increaseFragrance(appliedFragrance)

    '''
    '''
    def initializeHives(self):
        for i in range(self.numHives):
            searching = True
            while searching:
                index = random.randint(0, self._size ** 2)
                if (not self.board[index].isFoodSource()) and (not self.board[index].hasHive()):
                    self.board[index].addHive()
                    self.hiveLocations.append(self.indexToCoordinate(index))
                    searching = False

    '''
    '''
    def getHiveLocations(self):
        return self.hiveLocations

    '''
    updateFragrance: Cycles through all the tiles in the world and updates their fragrance levels.  
        This will be done whenever a food source is fully gathered so the bees don't get tricked.
        Note: I may make it whenever a food source drops by a certain percentage and apply it to only that source.
            I think that's actually what I'll do.
    args: none
    return:
        none
    Notes:
    1.  Cycles through all tiles on board
    2.  If tile contains food, generates a circle of radius where the minimum scent added is 1
    3.  Trims the circle's coordinates to fit the board.
    4.  Takes new list and adds fragrance at a rate of f(x) = fragrance / r^2
    '''
    def updateFragrance(self):
        for tile in self.board:
            if tile.isFoodSource():
                fragrance = tile.getFragrance()
                radius = round((10 * fragrance) ** 0.5)
                origin = self.indexToCoordinate(self.board.index(tile))
                coordList = self.coordinateFilter(self.circleArea(origin, radius))
                for entry in coordList:
                    if entry == origin:
                        appliedFragrance = fragrance
                        continue
                    dist = self.distance(entry, origin)
                    appliedFragrance = fragrance / (dist ** 2)
                    entry.increaseFragrance(appliedFragrance)

    '''
    indexToCoordinate: converts an index into the associated coordinate pair
    args: index
        index is the index of a specific tile
    return:
        returns the (x, y)
    '''
    def indexToCoordinate(self, index):
        x = (index % self._size) + 1
        y = int(((index - (index % self._size)) / self._size) + 1)
        return (x, y)

    '''
    coordinateToIndex: converts a coordinate tuple into the associated index
    args: coordinates
        coordinates is a tuple of (x, y)
    return:
        returns the associated index for that coordinate pair
    '''
    def coordinateToIndex(self, coordinates):
        x, y = coordinates
        x -= 1
        y -= 1
        index = (y * self._size) + x
        return index

    '''
    initializeBoard: generates tiles for every slot on the board
    args: none
    return: none
    '''
    def initializeBoard(self):
        for i in range(self._size ** 2):
            self.board.append(Tile(self.indexToCoordinate(i)))


    '''
    coordinateFilter: takes a list of coordinates, and filters out invalid ones based on board
    args: coordList
        coordList is a list of tuple coordinates in (x, y) format.
    return:
        an updated list of coordinates with all out of bounds coordinates deleted.
    '''
    def coordinateFilter(self, coordList):
        maxX = self._size
        maxY = self._size
        trimmedList = []
        for entry in coordList:
            if entry[0] >= 0 and entry[0] < maxX and entry[1] >= 0 and entry[1] < maxY:
                trimmedList.append(entry)
        return trimmedList

    '''
    getSize: returns the size of one side of the board
    args: none
    return: 
        returns the size of the board
    '''
    def getSize(self):
        return self._size


    '''
    '''
    def getFoodLocations(self):
        return self.foodLocations

    '''
    getTile: returns the tile at a location
    args: coordinates
        coordinates is a tuple in (x, y) format indicating the location of the tile
    return:
        returns the tile at the given location
    '''
    def getTile(self, coordinates):
        return self.board[self.coordinateToIndex(coordinates)]

    '''
    getBoardData: Returns a desired set of data from the board
    args: dataType
        dataType is the type of data that is desired from the board.
    return:
        Returns a list of coordinate pairs with the desired data.
    '''
    def getBoardData(self, dataType = "standard"):
        boardData = []
        for tile in self.board:
            index = self.board.index(tile)
            if dataType == "fragrance":
                data = tile.getFragrance()
            elif dataType == "standard":
                data = tile.getFood()
            else:
                print("Invalid dataType")
            entry = [tile.getCoordinates(), data]
            boardData.append(entry)
        return boardData

    '''
    circleArea: generates a list of all the coordinates that fall within a circle of given radius/origin
    args: origin, radius
        origin is a coordinate pair in (x, y) format that marks the center of a circle
        radius is the radius of the circle
    return:
        a list of coordinates that fall within the area of a circle.  Does not account for world border.
    Notes:
        Circle Equation: (x-h)^2 + (y-k)^2 = r^2
        Knowns: y, h, k, r.  solve for x
        x^2 - 2xh + h^2 = r^2 - (y-k)^2 for (y = k - r to y = k + r)
        x^2 -2xh = r^2 - h^2 - (y-k)^2
        x^2 - 2xh = constant - (y-k)^2
        x^2 - 2xh - constant + (y-k)^2 = 0
    '''
    def circleArea(self, origin, radius):
        coordList = []
        h, k = origin
        constant = (radius ** 2) - (h ** 2)
        for y in range(k - radius, k + radius):
            for x in range(h - radius, h + radius):
                if (x ** 2) - (2 * x * h) - constant + ((y - k) ** 2) <= 0.1:
                    coordList.append((x, y))
        return coordList

    '''
    distance: returns the distance between two coordinates
    args: coord1, coord2
        coord1 is the first pair of [y,x] coordinates
        coord2 is the second pair of [y,x] coordinates
    return:
        returns a double value that's the distance between the two points
    '''
    def distance(self, coord1, coord2):
        x1 = coord1[1]
        x2 = coord2[1]
        y1 = coord1[0]
        y2 = coord2[0]
        distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
        return distance