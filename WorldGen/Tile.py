# -*- coding: utf-8 -*-


import random

class Tile:
    def __init__(self, coordinates):
        self.location = coordinates
        self.hive = False

        #Is this tile a food source?
        if random.random() > 0.99:
            self.foodSource = True
            self.availableFood = int(random.gauss(50, 10))
            self.fragrance = float(self.availableFood)
        else:
            self.foodSource = False
            self.availableFood = 0
            self.fragrance = 0.00
        self.originalFood = self.availableFood

    #Getters
    def getX(self):
        return self.location[0]

    def getY(self):
        return self.location[1]

    def isFoodSource(self):
        return self.foodSource

    def getFood(self):
        return self.availableFood

    def getFragrance(self):
        return self.fragrance

    def getCoordinates(self):
        return self.location

    #Modifiers

    #adds to fragrance.
    def increaseFragrance(self, val):
        self.fragrance += val

    #removes from fragrance (could be done by passing a negative value, but this is more clear I feel)
    def reduceFragrance(self, val):
        self.fragrance -= val

    #Reduces food in the tile.
    def foodReduce(self):
        self.availableFood += 1
        if self.availableFood <= 0:
            self.foodSource = False

    #Display
    def displayInfo(self):
        print("Internal Information:")
        print("Coordinates: " + self.location)
        print("Food Source: " + str(self.foodSource))
        print("Available Food: " + str(self.availableFood))
        print("Fragrance: " + str(self.fragrance))

    #OVERRIDES

    def print(self):
        print(self.availableFood)