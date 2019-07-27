from WorldGen.World import World

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
    newFile = open(r"SaveData/worldData.txt", "w")
    newFile.write(displayWorldsCondensed(worldList))
    newFile.close()

def autoSetup():
    numOfWorlds = 1
    size = "medium"
    return numOfWorlds, size

def manualSetup():
    numOfWorlds, size = setParameters()
    return numOfWorlds, size

def setParameters():
    numOfWorlds = int(input("How many worlds would you like to initialize?\n"))
    size = input("Select a map size: small/medium/large\n")
    return numOfWorlds, size

def setup():
    setup = int(input("Choose manual setup (0) or automatic setup (1):\n"))
    if setup == 0:
        return "manual"
    elif setup == 1:
        return "auto"
    else: #should never occur
        return 0

def initalizeWorlds(numOfWorlds, size):
    worldList = []
    for i in range(numOfWorlds):
        worldList.append(World(size))
    return worldList

def displayWorlds(worldList):
    for world in worldList:
        world.displayCondensed()

def sizeConversion(size):
    if size == "small":
        return 500
    elif size == "medium":
        return 1000
    elif size == "large":
        return 2000
    else:
        return 0

def execute():
    setupSelection = setup()
    if setupSelection == "manual":
        numOfWorlds, size = manualSetup()
    elif setupSelection == "auto":
        numOfWorlds, size = autoSetup()

    worldList = initalizeWorlds(numOfWorlds, sizeConversion(size)) #array of worlds involved in simulation
    return