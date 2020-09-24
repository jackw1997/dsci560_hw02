# This is a python script that can generate some random number within 0 to 100

import numpy as np

rand_numbers = np.random.rand(1000) * 100

with open('hw02_1a.txt', 'w') as f:
    for i in range(1000):
        f.write('{}\n'.format(rand_numbers[i]))