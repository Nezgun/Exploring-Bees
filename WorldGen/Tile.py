# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:34:29 2019

"""
import random
import math

class Tile:
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y

        #Is this tile a food source?
        if random.random() > 0.99:
            self.foodSource = True
            self.availableFood = int(random.gauss(50, 10))
            self.fragrance = float(self.availableFood)
        else:
            self.foodSource = False
            self.availableFood = 0
            self.fragrance = 0.00

    #Getters
    def getX(self):
        return self.xCoord

    def getY(self):
        return self.yCoord

    def isFoodSource(self):
        return self.foodSource

    def getFood(self):
        return self.availableFood

    def getFragrance(self):
        return self.fragrance

    def getCoordinates(self):
        return self.xCoord, self.yCoord

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

    #Interactors
    #Adds fragrance to nearby tiles Circules around self using rate of Fragrance * (1/r^2)
    def addFragrance(destination):
        return

    def distance(self, destination):
        x1 = self.xCoord
        y1 = self.yCoord
        x2, y2 = destination.getCoordinates()
        return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)) 

    #Display
    def displayInfo(self):
        print("Internal Information:")
        print("Coordinates: (" + str(self.xCoord) + ", " + str(self.yCoord) + ")")
        print("Food Source: " + str(self.foodSource))
        print("Available Food: " + str(self.availableFood))
        print("Fragrance: " + str(self.fragrance))

    #OVERRIDES

    def print(self):
        print(self.availableFood)