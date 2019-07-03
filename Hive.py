# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:15:19 2019

"""

class Hive:
    def __init__(self):
        self.location = [0, 0]
        #Bees Total = home plus away
        #Home Bees
        #Away Bees
        foodSupply = 0
        #Memory
        #KeyMemory
        return

    def getLocation(self):
        return self.location

    def createBee(self):
        if self.foodSupply > 0:
            self.foodSupply -= 1
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