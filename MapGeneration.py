# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:22:54 2019

"""

import numpy as np
import Tile

class world:
    
    def __init__(self):
        self.board = np.empty([1000, 1000], Tile)      