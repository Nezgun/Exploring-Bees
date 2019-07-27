from Main_Directory.simulation import Simulation
from Main_Directory.Displays.DisplayFunctions import *
from Main_Directory.mainFunctions import *

#WorldGen Test
'''
testWorld = World()
fragranceMap_2D(testWorld)
'''

#WorldGen/Simulation Test
instance1 = Simulation()
testWorld = instance1.getWorld()
fragranceMap_2D(testWorld)