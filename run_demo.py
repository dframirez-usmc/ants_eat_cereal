# PROBLEM 1

# ASSUMPTIONS:
# All ants spawn from the same "ant hole"
# Ant hole is at a static coordinate (50,50)

# Although asking questions could clarify these assumptions, 
# I made the judgement call that the impact on the overall 
# objective, evaluation of coding proficiency, is minimal.
# I believe your time is more valuable in this circumstance.

# Dependencies:
#   numpy
#   pandas

# Configuration Settings
n_tests = 1000
show_state = False 
# Standard Output visualization of grid simulation world
# Works best when World.size = (10,10)

import time
import os
from ants_eat_cereal import *
from multiprocessing import Pool
import numpy as np

start_time = time.time()
result_objs = []
# Number for processes to use for computations
if show_state == False:
    processes = os.cpu_count()-1
elif show_state == True:
    processes = 1
# Multiprocessor if show_state is set False

# Monte Carlo Simulation
with Pool(processes) as pool:
    for n in range(n_tests):
        result = pool.apply_async(Ant_Simulation, (n, show_state))
        result_objs.append(result)
    test_results = [result.get() for result in result_objs]

print("---- Total Simulation Time: %s sec ----" % (round(time.time() - start_time, 3)))
print("---- Eaten Food Mean of",n_tests,"runs:",round(np.mean(test_results),3),"----")
print("---- Standard Deviation of",n_tests,"runs:",round(np.std(test_results),3),"----")