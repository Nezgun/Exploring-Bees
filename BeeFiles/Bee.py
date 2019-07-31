# -*- coding: utf-8 -*-

#from DataStorageSystems.Stack import Stack
#from DataStorageSystems.LinkedList import LinkedList

class Bee(object):
    def __init__(self, location, name, home):
        #General Bee Metadata
        self._home = home
        self._name = name #Bee's ID
        self.location = None #Current location => starts in hive

        #importantMemory
        #genericMemory linkedlist
        #self.generalMemory = LinkedList()
        #hiveMemory
        #movementQueue