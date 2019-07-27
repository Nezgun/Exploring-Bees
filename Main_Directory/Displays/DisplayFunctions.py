import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from Main_Directory.WorldGen.World import World

def fragranceMap_2D(world):
    xList = np.arange(world.getSize())
    yList = np.arange(world.getSize())
    displayData = world.getBoardData("fragrance")
    fragranceData = []
    for entry in displayData:
        fragranceData.append(entry[1])
    X, Y = np.meshgrid(xList, yList)
    Z = np.array(fragranceData)
    Z = Z.reshape((world.getSize(), world.getSize()))

    #Linear
    plt.figure(1)
    fragrancePlot = plt.contourf(X, Y, Z)
    plt.colorbar()
    plt.title('Fragrance Plot (Linear)')
    plt.xlabel('x')
    plt.ylabel('y')
    
    #Log
    plt.figure(2)
    fragrancePlot = plt.contourf(X, Y, Z, locator=mpl.ticker.LogLocator())
    plt.colorbar()
    plt.title('Fragrance Plot (Log)')
    plt.xlabel('x')
    plt.ylabel('y')

    #Displays
    plt.show()
