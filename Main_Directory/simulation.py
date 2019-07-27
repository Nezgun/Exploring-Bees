'''
The simulation object will hold all the data for a full simulation and will import what is necessary.
'''

from Main_Directory.WorldGen.World import World

from Main_Directory.BeeFiles.Hive import Hive

class Simulation(object):
    def __init__(self):
        self._world = World()
        self.hiveList = []
        hiveLocations = self._world.getHiveLocations()
        for location in hiveLocations:
            self.hiveList.append(Hive(self._world, location))
        self.turns = 0
    
    def displaySimulationData(self):
        return

    def getWorld(self):
        return self._world