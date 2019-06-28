from WorldGen.World import World

class Bee:
    def __init__(self, world, hive):
        self.world = world
        self.affiliation = hive
        self.location = self.affiliation.getLocation()
        self.carriedFood = 0
        #importantMemory
        #genericMemory
        #hiveMemory

        return

    def explore():
        return

    def pinpoint():
        return

    def alert():
        return

    def pickDirection():
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

    def action():
        return

    def gather(self):
        self.world.gatherFood(self.location)
        return

    def updateHive():
        return

    def updateSelf():
        return

    def remember():
        return