import pandas as pd
import numpy as np
import random
from typing import Tuple
import copy
import operator
import gc

class Location(object):
    def __init__(self):
        self.ants = []
        self.food = None
    def add_ant(self):
        self.ants.append(Ant)
    def add_food(self):
        self.food = Food # TODO Get nutritional infomation of cereal
    def del_ants(self):
        while Ant in self.ants:
            del self.ants[-1] # Deep delete the objects to prevent a potential memory leak
    def del_food(self):
        if self.food:
            self.food = None
    def __repr__(self):
        if self.ants:
            return 'A'
        elif self.food:
            return 'F'
        else:
            return ' '
    def __str__(self):
        if self.ants:
            return 'A'
        elif self.food:
            return 'F'
        else:
            return ' '

class Food(object):
    def __init__(self, food_type:str = 'cereal', cereal_df:pd.DataFrame = None):
        self.food_type = food_type
        if cereal_df is not None:
            # Get the nutrition info for a particular type of cereal
            self.nutrition = cereal_df[cereal_df['name']==self.food_type].to_dict()
        else:
            self.nutrition = None

class Ant(object):
    # TODO Track each Ant's calorie intake
    pass

class World():
    def __init__(self, 
                 size:Tuple[int, int]=(100,100), 
                 ant_loc:Tuple[int,int]=(50,50), 
                 n_ants:int = 100, 
                 n_foods:int = 10, 
                 cereal_df:pd.DataFrame = None):
        self.size = size
        x_max_idx,y_max_idx = size
        self.x_max_idx = x_max_idx-1
        self.y_max_idx = y_max_idx-1

        # Initilize world
        #locations = np.vectorize(Location) # Not working consistently
        self.state = np.ndarray(self.size, dtype=object) # Initilize state array
        for x,y in np.ndindex(self.size):
            self.state[x,y] = Location() # Place Locations objects into state array

        # Set Food locations
        rand_locs = set() #sets don't duplicate values
        while len(rand_locs) < n_foods:
            x = random.randint(0, self.x_max_idx)
            y = random.randint(0, self.y_max_idx)
            rand_locs.add((x,y))
        for x,y in rand_locs:
            if cereal_df is not None:
                food_type = cereal_df['name'].sample() # Choose/sample random cereal type
            else:
                food_type = 'cereal'
            self.state[x,y].add_food()
            #self.state[x, y].add_thing(Food(food_type, cereal_df)) # TODO Bug when initilizing objects with atributes
        self.food_eaten = 0
        
        # Set Ant locations
        for i in range(n_ants):
            self.state[ant_loc[0],ant_loc[1]].add_ant()
        self.ant_count = n_ants

    def print_state(self):
        print(self.state)
        print('Food Eaten =',self.food_eaten)
        #print('Ants =',self.ant_count)
        #time.sleep(0.01) # For delay in animation

    def step(self):
        # Create new array for ants to move to
        # Standard copy operation only copies pointers to objects
        # Must complete above before proceeding to Ant movement
        next_state = copy.deepcopy(self.state) # DeepCopy for more than object pointers
        moves = [(1,0),(-1,0),(0,1),(0,-1)] # Movement options
        for x, y in np.ndindex(self.size):
            next_state[x,y].del_ants() # Clean up the new array removing ants
        # Move every Ant and eat food at new location
        for x, y in np.ndindex(self.size):
            # For all ants in each location
            for ant in self.state[x,y].ants:
                rand_move = moves[random.randint(0,len(moves)-1)]
                new_xy = tuple(map(operator.add, (x,y), rand_move)) # Sum tuples into new tuple
                # Only move ants into valid array index
                # If move is invalid Ant stays put
                if int(new_xy[0]) < 0:
                    next_state[x,y].add_ant()
                elif int(new_xy[1]) < 0:
                    next_state[x,y].add_ant()
                elif int(new_xy[0]) > self.x_max_idx:
                    next_state[x,y].add_ant()
                elif int(new_xy[1]) > self.y_max_idx:
                    next_state[x,y].add_ant()
                else: # Move is not invalid
                    next_state[new_xy].add_ant() # Move ant
                    # Check for food at new location
                    if next_state[new_xy].food:
                        next_state[new_xy].del_food()
                        self.food_eaten += 1

        del self.state # Potential for memory leak due to orphaned objects
        gc.collect() # Call the garbage collector to cleanup orphaned objects
        self.state = next_state
        
def Ant_Simulation(n_test, show_state):
    # Run a World Simulation
    print('Test:',n_test+1)
    #test_world = World(size=(10,10), ant_loc=(5,5))
    test_world = World(size=(100,100), ant_loc=(50,50))
    if show_state: test_world.print_state()
    for t in range(100):
        test_world.step()
        if show_state: test_world.print_state()
        if show_state: print('Test:',n_test+1,'Time Step:',t+1)
    return test_world.food_eaten