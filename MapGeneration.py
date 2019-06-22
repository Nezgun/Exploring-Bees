# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:22:54 2019

"""

import numpy as np
from World import World

size = input("Select a map size: small/medium/large\n")
print(size + " size selected.")

if size == "medium":
    world1 = World(1000)

world1.displayBoard()

