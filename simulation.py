'''
The simulation object will hold all the data for a full simulation and will import what is necessary.
'''

from WorldGen.World import World

from BeeFiles.Hive import Hive

class Simulation(object):
    def __init__(self, size):
        self._size = size
        self._world = World()
        self.hiveList = []
        hiveLocations = self._world.getHiveLocations()
        for location in hiveLocations:
            self.hiveList.append(Hive(location))
        self.turns = 0
    
    def displaySimulationData(self):
        return

    def getWorld(self):
        return self._world