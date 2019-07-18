import matplotlib as mpl
import matplotlib.pyplot as plt
from WorldGen.World import World

def fragranceMap(world):
    displayData = world.getBoardData("fragrance")
    coordList = [displayData[0] for row in displayData]
    dataList = [displayData[1] for row in displayData]
    plt.figure()
    fragrancePlot = plt.contour(coordList, dataList)