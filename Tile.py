# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:34:29 2019

@author: Mike Senpai
"""
import random

class Tile:
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y

        #Is this tile a food source?
        if random.random() > 0.90:
            self.foodSource = True
            self.availableFood = int(random.gauss(50, 10))
            self.fragrance = float(availableFood)
        else:
            self.foodSource = False
            self.availableFood = 0
            self.fragrance = 0.00


    #adds to fragrance.
    def increaseFragrance(val):
        self.fragrance += val

    #removes from fragrance (could be done by passing a negative value, but this is more clear I feel)
    def reduceFragrance(val):
        self.fragrance -= val

    #Adds fragrance to nearby tiles Circules around self using rate of Fragrance * (1/r^2)
    def addFragrance(destination):
        return

    #Reduces food in the tile.
    def foodReduce():
        availableFood += 1
        if availableFood <= 0:
            foodSource = False

    def distance(destination):
        x1 = xCoord
        y1 = yCoord
        x2, y2 = destination.getCoordinates()
        return

    def getCoordinates():
        return xCoord, yCoord