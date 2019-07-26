# -*- coding: utf-8 -*-

#from WorldGen.World import World
#from DataStorageSystems.Stack import Stack
#from DataStorageSystems.LinkedList import LinkedList

class Bee(object):
    def __init__(self, world, hive):
        #General Bee Metadata
        self._world = world #World bee is instantiated to
        self._affiliation = hive #Hive to which bee belongs
        self._name = None #Bee's ID
        self.location = self._affiliation.getLocation() #Current location => starts in hive

        #importantMemory
        #genericMemory linkedlist
        #self.generalMemory = LinkedList()
        #hiveMemory
        #movementQueue