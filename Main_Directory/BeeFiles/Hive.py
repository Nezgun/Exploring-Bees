# -*- coding: utf-8 -*-

from Main_Directory.WorldGen.World import World
#Bee Imports
from Main_Directory.BeeFiles.Bee import Bee
from Main_Directory.BeeFiles.Queen import Queen
from Main_Directory.BeeFiles.Worker import Worker

class Hive:
    def __init__(self, world = World(), location = (0, 0)):
        self.location = [0, 0]
        self.world = world
        self.totalBees = 0
        self.bees = {}
        self.homeBees = {}
        self.awayBees = {}
        self.foodSupply = 10
        #Memory
        #KeyMemory
        return

    def initializeBees(self):
        return

    def getLocation(self):
        return self.location

    def createBee(self):
        if self.foodSupply > 0:
            self.foodSupply -= 1
            self.totalBees += 1
            #add a new bee to Home Bees
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