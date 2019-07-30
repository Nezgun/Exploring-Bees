# -*- coding: utf-8 -*-

from Main_Directory.BeeFiles.Bee import Bee

class Worker(Bee):
    def __init__(self):
        self.actionList = ['move', 'gather'] #List of available actions
        self.carriedFood = 0 #Amount of food carried by bee
        self.carryCapacity = 1 #Max amount a bee can carry
        self.noseSensitivity = 1 #Adjustable trait indicating sensitivity for sensing fragrance levels
        return

        #Actions
    def explore():
        return

    def pickDirection():
        return

    def pinpoint():
        #Called if tile fragrance > nose sensitivity
        #check 8 surrounding tiles, move to highest scent.  If no higher scent, pick at random.
        #Repeat until tile is food tile.
        return

    def alert():
        #First: Add coordinate to important memory with tag:food
        #Second: Plot Course back to hive and add it to the movement queue
        #Third: iterate through queue until return to the hive
        return

    def move(self, intDirect):
        intDirect %= 8
        if intDirect == 0: #N
            self.location[1] += 1
        elif intDirect == 1: #NE
            self.location[0] += 1
            self.location[1] += 1
        elif intDirect == 2: #E
            self.location[0] += 1
        elif intDirect == 3: #SE
            self.location[0] += 1
            self.location[1] -= 1
        elif intDirect == 4: #S
            self.location[1] -= 1
        elif intDirect == 5: #SW
            self.location[0] -= 1
            self.location[1] -= 1
        elif intDirect == 6: #W
            self.location[0] -= 1
        elif intDirect == 7: #NW
            self.location[0] -= 1
            self.location[1] += 1
        else:
            return
        return

    '''
    remember: If a tile is not a part of general memory, it is added to general memory.
    args: none
    return: none
    '''
    #def remember(self):
    #    tile = (self.location)
    #    if self.generalMemory.search(tile) == 0:
    #        self.generalMemory.insert(tile)
    #    else:
    #        return

    def action():
        return

    #Update Functions
    def updateHive():
        #dump information into hive
        #clear local memory
        return

    def updateSelf():
        #make copy of hive memory
        return

    #Query Functions
    def queryTile(self):
        return
