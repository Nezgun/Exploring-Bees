
from Tile import Tile
import numpy as np

class World:
    
    def __init__(self, size = 1000):
        self.size = size
        self.board = np.empty((size, size), Tile)

    def displayBoard():
        print(board)

