from simulation import Simulation
from DisplayFunctions import *
from mainFunctions import *

#WorldGen Test
'''
testWorld = World()
fragranceMap_2D(testWorld)
'''

#WorldGen/Simulation Test
instance1 = Simulation(100)
testWorld = instance1.getWorld()
fragranceMap_2D(testWorld)