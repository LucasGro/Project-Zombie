import numpy as np

from init import initialize
from simulation import run_simulation

map2d = np.zeros([100, 100])
humans, zombies = initialize()

result = run_simulation(humans, zombies, map2d)

