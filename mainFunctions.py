from WorldGen.World import World

def worldInitialization(size = 1000):
    return World(size)

def displayOverview(size, numOfWorlds):
    print("Initalization Overview")
    print(size + " size selected.")
    print(str(numOfWorlds) + " worlds will be generated.")

def sizeSelection(size):
    if size == "small":
        return 100
    elif size == "medium":
        return 1000
    elif size == "large":
        return 5000
    else:
        return 0

def displayWorldsCondensed(worldList):
    size = worldList[0].getSize()
    i = 1
    display = ""
    for entry in worldList:
        display += ("World " + str(i) + ":\n")
        display += entry.displayCondensed()
        display += (("+-" * (int((size/2))) * 3) + "\n")
        i += 1
    return display

def saveWorld(worldList):
    newFile = open(r"worldData.txt", "w")
    newFile.write(displayWorldsCondensed(worldList))
    newFile.close()
