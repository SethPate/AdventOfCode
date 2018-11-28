from floor import *

floors = {1: Floor(1), 2: Floor(2), 3: Floor(3), 4: Floor(4)}

floors[1].addGenerator('pro').addChip('pro')
floors[2].addGenerator('cob').addGenerator('cur').addGenerator('rut').addGenerator('plu')
floors[3].addChip('cob').addChip('cur').addChip('rut').addChip('plu')

