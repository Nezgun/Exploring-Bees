# -*- coding: utf-8 -*-

#from DataStorageSystems.Stack import Stack
#from DataStorageSystems.LinkedList import LinkedList

class Bee(object):
    def __init__(self, world, hive):
        #General Bee Metadata
        self._name = None #Bee's ID
        self.location = self._affiliation.getLocation() #Current location => starts in hive

        #importantMemory
        #genericMemory linkedlist
        #self.generalMemory = LinkedList()
        #hiveMemory
        #movementQueue