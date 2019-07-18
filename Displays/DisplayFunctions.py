import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from WorldGen.World import World

def fragranceMap_2D(world):
    xList = np.arange(world.getSize())
    yList = np.arange(world.getSize())
    displayData = world.getBoardData("fragrance")
    fragranceData = []
    for i in range(len(displayData)):
        fragranceData.append(displayData[i][1])
    X, Y = np.meshgrid(xList, yList)
    Z = np.array(fragranceData)
    Z = Z.reshape((world.getSize(), world.getSize()))
    print(Z.shape)

    plt.figure()
    fragrancePlot = plt.contourf(X, Y, Z, locator=mpl.ticker.LogLocator())
    plt.colorbar()
    plt.clabel(fragrancePlot, inline=False, fontsize=10)
    plt.title('Fragrance Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()