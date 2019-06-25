from mainFunctions import *
from WorldGen.World import World

#Manual or Auto Setup
numOfWorlds = int(input("How man worlds would you like to initialize?\n"))
size = input("Select a map size: small/medium/large\n")

displayOverview(size, numOfWorlds)

size = sizeSelection(size)
worldList = []
for i in range(numOfWorlds):
    worldList.append(World(size))

print(displayWorldsCondensed(worldList))

saveWorld(worldList)