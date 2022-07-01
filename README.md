# ants_eat_cereal
Interview project testing object oriented program and pandas

1. In a grid of 100 by 100 locations, randomly spawn 10 pieces of food. Food must not spawn on the same location.
2. Next spawn 100 ants, from 1 ant-hole location in the center of the location grid. Ants may occupy the same location.
3. On each time-step of the world, each ant moves randomly in one of the four cardinal directions. An ant may not exceed the edge of the location grid.
4. When an ant steps onto the location of the food, the food is removed from the locations grid.
5. Run the world through 100 time-steps.
6. How many pieces of the randomly spread food do the ants find?
7. Simulate this 1000 times a Monte Carlo experiment.
8. What is the mean and standard deviation of this simulations?

For this project I utilized:
- Python objects
- Objects which hold state
- Numpy arrays of state objects
- DeepCopy to create next time step state
- Object interaction
- Deleting objects to free memory
- Garbage collection
- Multiprocessing
- Pandas
- Filtering
- Pandas plotting
