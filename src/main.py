import numpy as np
from init import initialize
from simulation import run_simulation

map_2d = np.zeros([100, 100])

print(map_2d)

human_list, zombie_list = initialize()
print(human_list, zombie_list)
run_simulation()
