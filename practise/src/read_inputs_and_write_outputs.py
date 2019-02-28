# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:59:50 2019

@author: Sage
"""
import os
import models
import numpy as np


out_folder = '../out/unidim/'
try:
    os.makedirs(out_folder)
except OSError:
    if not os.path.isdir(out_folder):
        raise

pizza_paths = ['../a_example.in', '../b_small.in', '../c_medium.in',
               '../d_big.in']

for pizza_path in pizza_paths:
    print ('Pizza file: %s' % pizza_path)
    f = open(pizza_path, mode='r')

    header = f.readline()
    row_count, column_count, min_ingredient, max_area = tuple(map(
            int, header.split(' ')))

    grid = []
    for i in range(row_count):
        grid.append(list(f.readline().rstrip()))
    grid = np.array(grid)
    f.close()

    results = models.unidimensional_greedy_heuristic(row_count, column_count, min_ingredient, 
                                                     max_area, grid)

    f = open(out_folder + pizza_path.split('/')[-1], mode='w')
    f.write(str(len(results)) + '\n')
    f.writelines(map(lambda x: ' '.join(map(str, x)) + '\n', results))
    f.close()
    print ('\n')
