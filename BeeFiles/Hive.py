# -*- coding: utf-8 -*-

#Bee Imports
from BeeFiles.Bee import Bee
from BeeFiles.Queen import Queen
from BeeFiles.Worker import Worker

class Hive:
    def __init__(self, location):
        self._location = location
        self.totalBees = 1
        #self.queen = Queen(self._location, "Queen", self._location)
        self.bees = {}
        self.homeBees = {}
        self.awayBees = {}
        self.foodSupply = 10
        #Memory
        #KeyMemory
        return

    #Getters

    def getLocation(self):
        return self._location

    #Modifiers

    def createBee(self):
        if self.foodSupply > 0:
            self.foodSupply -= 1
            self.totalBees += 1
            #add a new bee to Home Bees
        return

    #Utilities

    #Initialization

    def initializeBees(self):
        return

'''
Properties:
Home Bees (dictionary of bees in the hive)
= 10 to start
Away Bees (dictionary of bees away)
Food Supply (int)
This is what we’re trying to optimize
Memory (dict of arrays)
(dict of coordinates we’ve discovered)
Key Memory (dict of arrays)
(secondary memory of areas with food)
Create Bee
Removes 1 food to create a new bee.
Functions:
	Dispatch Bee()
'''